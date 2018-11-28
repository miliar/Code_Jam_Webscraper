#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
typedef long long ll;

ifstream fin ("A.in");
ofstream fout ("A.out");

string P[14], R[14], S[14];
int N, np, nr, ns;

bool good (string s)
{
	int cp = 0, cr = 0, cs = 0;
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == 'P')
			cp++;
		else if (s[i] == 'R')
			cr++;
		else
			cs++;
	}

	return cp == np && cr == nr && cs == ns;
}

int main()
{
	P[0] = "P";
	R[0] = "R";
	S[0] = "S";

	for (int i = 0; i < 13; i++)
	{
		if (P[i+0] < R[i+0])
			P[i+1] = P[i+0] + R[i+0];
		else
			P[i+1] = R[i+0] + P[i+0];

		if (P[i+0] < S[i+0])
			S[i+1] = P[i+0] + S[i+0];
		else
			S[i+1] = S[i] + P[i];

		if (R[i] < S[i])
			R[i+1] = R[i] + S[i];
		else
			R[i+1] = S[i] + R[i];
	}

    int ntest = 0; fin >> ntest;
    for (int test = 1; test <= ntest; test++)
    {
    fin >> N >> nr >> np >> ns;
    
    fout << "Case #" << test << ": ";
    if (good (P[N]))
    	fout << P[N];
    else if (good (R[N]))
    	fout << R[N];
    else if (good (S[N]))
    	fout << S[N];
    else
    	fout << "IMPOSSIBLE";
    fout << "\n";
    }
    return 0;
}

