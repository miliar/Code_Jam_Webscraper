#include "fstream"
#include "vector"
#include <iostream>
#include <algorithm>
#include <math.h> 
#include <map> 

using namespace std;

static map<long long unsigned int, long long unsigned int> myMapPrime;
static map<long long unsigned int, long long unsigned int> myMapNonPrime;


bool isPrime(long long unsigned int n,long long unsigned int &div)
{

	map<long long unsigned int, long long unsigned int>::iterator itMapPrime = myMapPrime.find(n);
	if (itMapPrime != myMapPrime.end())
		return false;

	map<long long unsigned int, long long unsigned int>::iterator itmapNonPrime = myMapNonPrime.find(n);
	if (itmapNonPrime != myMapNonPrime.end())
	{
		div = itmapNonPrime->second;
		return true;
	}


	bool flag = false;
	long long unsigned int i = 2;
	for (; i <= n / 2 && i<100; ++i)
	{
		if (n%i == 0)
		{
			flag = true;
			div = i;
			myMapNonPrime.insert(pair<long long unsigned int, long long unsigned int>(n, div));
			break;
		}
	}	

	if (!flag)
	{
		myMapPrime.insert(pair<long long unsigned int, long long unsigned int>(n, 0));

	}

	return !flag;
}

long long unsigned int Base(int* v,int N,int base)
{
	long long unsigned int sum = 0;
	for (int i = 0; i < N; i++)
	{
		sum += v[i]*pow(base, i);
	}
	return sum;
}

void createBinaryNum(int* v,int n,int N,int &J,int digit)
{

	if (J == 0)
	{
		return;
	}

	v[N] = digit;
	if (N == 0)
	{
		vector<long long unsigned int > results;
		v[N] = 1;
		bool flag = true;
		for (int base = 2; base <= 10 && flag; base++)
		{
			long long unsigned int num = Base( v, n, base);
			long long unsigned int div;
			bool prime = isPrime(num, div);
			if (prime)
			{
				results.clear();
				flag = false;
				break;
			}
			else
			{
				results.push_back(div);
			}
		}
		if (flag)
		{
			ofstream outputFile;
			outputFile.open("result", fstream::app);

			for (int i = n-1; i >= 0; i--)
			{
				cout << v[i];
				outputFile << v[i];
			}
			for (int i = 0; i < results.size(); i++)
			{
				cout << " " << results[i];
				outputFile << " " << results[i];
			}
			cout << endl;
			outputFile << endl;
			//outputFile.close();

			J--;

		}

		return;
	}
	createBinaryNum(v,n,N - 1,J, 1);
	if(N-1!=0)
		createBinaryNum(v,n,N - 1,J, 0);

}

int main()
{

	ifstream inputFile;
	inputFile.open("C-small-attempt4.in");
	//inputFile.open("Test.txt");
	ofstream outputFile;
	outputFile.open("result");
	vector<int> myMap;
	int T;
	inputFile >> T;
	int* v;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": " << endl;
		outputFile << "Case #" << t << ": " << endl;
		//outputFile.close();
		int N;
		inputFile >> N;
		int J;
		inputFile >> J;
		v = new int[N];
		createBinaryNum(v, N,N,J, 1);



//		cout << "Case #" << t << ": " << c << endl;
		//outputFile << "Case #" << t << ": " << c << endl;

	}
	return 0;
}
