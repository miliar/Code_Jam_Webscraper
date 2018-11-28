#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

#define LL long long

class NumberTheory
{ public:

	// GLOBALS
	bool Fun_Debug_Enabled, Std_Debug_Enabled, Err_Debug_Enabled, Stats_Debug_Enabled;
	int Iterations_Stop;
	int T;

	// CONSTRUCTOR
	NumberTheory(string setup)
	{
		if (setup == "CountingSheep")
		{
			freopen ("CountingSheep.in", "r", stdin);
			cin >> T;	
			//freopen ("CountingSheep.out", "w", stdout);
		}
		else if (setup == "CoinJam")
		{
			freopen ("CoinJam.in", "r", stdin);
			cin >> T;
			freopen ("CoinJam.out", "w", stdout);
		}
	}

	// LOGGING
	void Log_Fun(string message) { if (Fun_Debug_Enabled) cout << message << endl; }
	void Log_Std(string message) { if (Std_Debug_Enabled) cout << message << endl; }
	void Log_Err(string message) { if (Err_Debug_Enabled) cout << message << endl; }
	void Log_Stats(string message) { if (Stats_Debug_Enabled) cout << message << endl; }
	void Log_Err_Exit(string message) { cout << message << endl; exit(0); }

	string VectorToString(vector <int> my_vector)
	{
		stringstream result;
		copy(my_vector.begin(), my_vector.end(), ostream_iterator<int>(result, " "));
		string all = result.str();
		return all.substr(0, all.length() - 1);
	}

	string VectorToString(vector <LL> my_vector)
	{
		stringstream result;
		copy(my_vector.begin(), my_vector.end(), ostream_iterator<LL>(result, " "));
		string all = result.str();
		return all.substr(0, all.length() - 1);
	}

	string NumberToBinary(LL num, int digits)
	{
		string binary = "";
		for (int i = digits - 1; i >= 0; --i)
			if (num & (1<<i)) binary += "1";
			else binary += "0";

		return binary;
	}

	// NUMBER APPLIERS
	int GetNx(int N, int x) { return N * (x + 1); }
	int GetNext(int prev, int N) { return prev + N; }
	int LastDigit(int num) { return num % 10; }
	int WithoutLastDigit(int num) { return num / 10; }

	// VECTOR APPLIERS
	// filling = "Num "means you decompose the number into digit counts
	// The rest of the cases fill with given num
	vector <int> GetC(int num, string filling = "Num")
	{
		vector <int> retC(10);

		if (filling == "Num")
		{
			fill(retC.begin(), retC.end(), 0);
			do 
			{
				int lastDigit = LastDigit(num);
				retC[lastDigit]++;
				num = WithoutLastDigit(num);
			}
			while (num != 0); // check if you can improve the do-while
		}
		else fill(retC.begin(), retC.end(), num);
		return retC;
	}

	vector <int> GetRC(vector<int> R, vector<int> C)
	{
		if (R.size() != C.size()) Log_Err_Exit("ERROR in GetRC");
		vector <int> RC(R.size());
		for (int i = 0; i < RC.size(); ++i) RC[i] = R[i] + C[i];
		return RC;
	} // to replace with transform

	bool AGreaterOrEqualB(vector <int> A, vector <int> B)
	{
		if (A.size() != B.size()) Log_Err_Exit("ERROR in CompareVectors");
		for (int i = 0; i < A.size(); ++i) if (A[i] < B[i]) return false;
		return true;
	} // maybe replace with simpler

	// ALGORITHM STEP APPLIERS
	bool CheckDaylight(int iterations)
	{
		Log_Fun("Checking daylight for iteration " + to_string(iterations));
		if (iterations >= Iterations_Stop) return true;
		return false;
	}


	int BruteforceSolve(int N)
	{
		Log_Std("Bruteforce: " + to_string(N));
		bool asleep = false;
		bool daylight = false;
		int iterations = 0;
		int Nx = N;
		vector <int> currentR = GetC(0, "Zeros");
		vector <int> ones = GetC(1, "Ones");

		while (!asleep && !daylight)
		{
			vector <int> currentC = GetC(Nx);
			currentR = GetRC(currentR, currentC);
			Log_Std(to_string(Nx) + " -> " + VectorToString(currentR) + " -> " + VectorToString(currentC));
			
			asleep = AGreaterOrEqualB(currentR, ones);
			if (asleep) 
			{
				Log_Stats("Solved for " + to_string(N) + " in iterations: " + to_string(iterations));
				return Nx;
			}

			Nx = GetNext(Nx, N);
			daylight = CheckDaylight(++iterations);
		}

		Log_Stats("Did not find an answer");
		return Nx;
	} // make the while look nicer

	vector <vector <LL> > MatrixMul(vector <vector <LL> > A, vector <vector <LL> > B, LL p)
	{
		int n = A.size();
		vector < vector<LL> > C(n, vector <LL> (n, 0LL));

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				for (int k = 0; k < n; ++k)
					C[i][j] = (C[i][j] + ((A[i][k] * B[k][j]) % p)) % p;

		return C;
	}

	vector < vector<LL> > MatrixPower(vector <vector <LL> > matrix, LL power, LL p)
	{
		int n = matrix.size();
		if (power == 0)
		{
			vector < vector<LL> > C(n, vector <LL> (n, 0LL));
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					C[i][j] = 1LL;
			return C;
		}
		else if (power == 1) return matrix;
		else
		{
			vector < vector<LL> > half = MatrixPower(matrix, power/2LL, p);
			vector < vector<LL> > whole = MatrixMul(half, half, p);
			if (power % 2LL) whole = MatrixMul(whole, matrix, p);
			return whole;
		}
	}

	LL PowerUp(LL a, LL power, LL p)
	{
		if (power == 0) return 1LL;
		else if (power == 1) return a;
		else
		{
			LL half = PowerUp(a, power/2LL, p);
			LL whole = (half * half) % p;
			if (power % 2LL) whole = (whole * a) % p;
			return whole;
		}
	}

	LL FibonacciN(LL N, LL p)
	{
		if (N == 0) return 0LL;

		int n = 2;
		vector < vector<LL> > C(n, vector <LL> (n, 1LL));
		C[0][0] = 0;
		vector < vector<LL> > Z = MatrixPower(C, N-1, p);
		LL FiboN = Z[1][1];
		return FiboN;
	}

	bool WeakPrimalityTest(LL p)
	{
		if (p % 5LL != 2 && p % 5LL != 3) return false;
		LL A = PowerUp(2LL, p-1, p);
		LL B = FibonacciN(p+1, p);
		if (A == 1 && B == 0) return true;
		return false; 
	}

	LL StrongPrimalityTest(LL p)
	{
		LL limit = (LL)sqrt(p) + 10;
		if (p % 2LL == 0) return 2LL;
		for (LL i = 3LL; i < limit; i += 2)
			if (p % i == 0) return i;
		return 0LL;
	}

	LL ConvertToBase(LL N, LL b, int digits)
	{
		LL mul = 1LL;
		LL result = 0LL;
		for (int i = 0; i < digits; ++i, mul *= b)
			if ((1<<i) & N) result += mul;

		return result;
	}

	vector <LL> GetBasedArr(LL config, int digits)
	{
		vector <LL> based_arr;
		for (int b = 2; b <= 10; ++b)
		{
			LL based = ConvertToBase(config, b, digits);
			based_arr.push_back(based);
		}
		return based_arr;
	}

	vector <pair<LL, vector <LL> > > CoinJamSmall(int N, int J, int digits)
	{
		vector <pair<LL, vector<LL> > > solutions;

		LL start = (1LL<<(digits-1)) + 1LL;
		LL stop = (1LL<<digits);
		for (LL config = start; config < stop; config += 2LL)
		{
			Log_Stats("Checking for " + NumberToBinary(config, digits));
			bool leave = false;
			vector <LL> based_arr = GetBasedArr(config, digits);

			for (int i = 0; i < based_arr.size(); ++i)
			{
				LL based = based_arr[i];
				Log_Stats("-> Checking for " + to_string(based));
				bool leave = WeakPrimalityTest(based);
				Log_Stats("-> -> Weak Primality: " + to_string(leave));
				if (leave) break;
			}
			if (leave) continue;

			Log_Stats("Weak Primality passed, checking strong");

			vector <LL> divisors;

			for (int i = 0; i < based_arr.size(); ++i)
			{
				LL based = based_arr[i];
				Log_Stats("-> Checking for " + to_string(based));
				LL divisor = StrongPrimalityTest(based);
				Log_Stats("-> -> Strong Primality: " + to_string(divisor));
				if (divisor == 0) 
				{
					leave = true;
					break;
				}
				divisors.push_back(divisor);
			}
			if (leave) continue;

			solutions.push_back(make_pair(config, divisors));
			if (solutions.size() == J) 
			{
				Log_Stats("Found all!");
				return solutions;
			}
		}
		return solutions;
	}

	// RUNNERS
	int CountSheep()
	{
		Err_Debug_Enabled = false;
		Stats_Debug_Enabled = false;
		Std_Debug_Enabled = false;
		Fun_Debug_Enabled = false;

		Iterations_Stop = 1000;

		int N;
		for (N = 1; N <= 1000000; ++N)//while(T--)
		{
			//cin >> N;
			int answer = BruteforceSolve(N);
			cout << answer << endl;
		}

		return 0;
	}

	int CoinJam()
	{
		Err_Debug_Enabled = false;
		Stats_Debug_Enabled = false;
		Std_Debug_Enabled = false;
		Fun_Debug_Enabled = false;

		int N, J;
		while(T > 0)
		{
			cout << "Case #" << T << ":" << endl;
			cin >> N >> J;
			int digits = N;
			vector <pair<LL, vector <LL> > > solutions = CoinJamSmall(N, J, digits);
			//cout << solutions.size() << endl;
			for (int i = 0; i < solutions.size(); ++i)
			{
				Log_Stats(NumberToBinary(solutions[i].first, digits));
				Log_Stats(VectorToString(solutions[i].second));
				cout << NumberToBinary(solutions[i].first, digits) << " " << VectorToString(solutions[i].second) << endl;

			}
			T--;
		}

		return 0;
	}
};

int main()
{
	int status;

	/*
	NumberTheory solver("CountingSheep");
	status = solver.CountSheep();
	if (status == 0) cout << "Successfully counted the sheep and finally fell asleep" << endl;
	// Log max, average, etc. of iterations
	// Put output in right format for submitting
	*/
	NumberTheory solver("CoinJam");
	solver.CoinJam();

	return 0;
}

