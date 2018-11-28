// CodeJamA.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;
#define length 1

vector<int> output;

void SolveForShyness()
{
	int Smax;
	string line;
	string SVectorString;
	getline(cin, line);
	stringstream stream(line);
	stream >> Smax;
	stream >> SVectorString;

	vector<int> SVector;
	size_t i = 0;
	while (i < SVectorString.size())
	{
		string S = SVectorString.substr( i, length );
		SVector.push_back(atol(S.c_str()));
		i += length;
	}
	long friends = 0;
	long sum = 0;
	for (size_t p = 0; p < SVector.size(); p++)
	{
		if (p == 0)
		{
			sum += SVector[p];
			continue;
		}

		if(sum < p)
		{
			friends += p - sum;
			sum = p;
		}

		sum += SVector[p];
	}
	output.push_back(friends);
}

int main()
{
	int T;
	ios::sync_with_stdio(false);
	cin >> T;
	cin.ignore();
	for (int i = 0; i < T; ++i)
	{
		SolveForShyness();
	}

	int p = 0;
	for (vector<int>::iterator it = output.begin(); ++p, it != output.end(); ++it)
		cout << "Case #"<<p<<": " << *it << "\n";
}
