#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int  SolveCase(string S)
{
	int numOfFlips = 0;
	for(int i = 0; i < S.length()-1; i++)
	{
		if(S[i] != S[i+1]) numOfFlips++;
	}
	
	if(S[S.length()-1] == '-') numOfFlips++;
	
	return numOfFlips;
}

int main()
{
	FILE *fin = freopen("B.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B.out", "w", stdout);

	int testCases;
	cin >> testCases;
	for(int t = 1; t <= testCases; t++)
	{
		string S;
		cin >> S;

		cout << "Case #" << t << ": ";
		cout << SolveCase(S) << endl;
	}

	exit(0);
}
