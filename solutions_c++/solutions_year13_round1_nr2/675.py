#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
using namespace std;

long long utility(long long E, long long R, int N, vector<long long>& v)
{
	if (N == 10)
		R = R;

	long long result = 0;
	int toDo = 0;
	long long energy = E;
	long long lookAhead = E/R+1;
	while (toDo < N)
	{
		int nextBig;
		for (nextBig = 1; nextBig < lookAhead && toDo+nextBig < N; nextBig++)
		{
			if (v[toDo+nextBig] > v[toDo])
				break;
		}

		if (nextBig < lookAhead && toDo + nextBig < N)
		{
			if (energy > E-nextBig*R)
			{
				result += (energy-E+nextBig*R)*v[toDo];
				energy = E;
				toDo += nextBig;
			}
			else
			{
				energy += nextBig*R;
				toDo += nextBig;
			}
		}
		else
		{
			result += energy*v[toDo];
			energy = min(E, R);
			toDo++;
		}
	}
	return result;
}

int main(int argv, char*argc)
{
	ifstream infile("test.txt");
	ofstream outfile("result.txt");
	if (!infile || !outfile)
	{
		cout << "wrong" << endl;
		return -1;
	}

	int numCase;
	infile >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		long long E, R, vTemp;
		int N;
		vector<long long> v;

		if (i == 99)
			i = i;

		infile >> E >> R >> N;
		for (int j = 0; j < N; j++)
		{
			infile >> vTemp;
			v.push_back(vTemp);
		}

		long long result = utility(E, R, N, v);
		outfile << "Case #" << i+1 << ": " << result << endl;
	}
	infile.close();
	outfile.close();
}