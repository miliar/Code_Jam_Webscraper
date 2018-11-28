#include <bits/stdc++.h>

using namespace std;

char checkString (string s)
{
	if (s.size() == 1) return 1;
	string s2 = "";
	int i;
	int N = s.size();
	for (i = 0; i < N; i+=2)
	{
		if (s[i] == s[i+1]) return 0;
		if ((s[i] == 'R') && (s[i+1] == 'P')) s2 += "P";
		if ((s[i] == 'R') && (s[i+1] == 'S')) s2 += "R";
		if ((s[i] == 'P') && (s[i+1] == 'R')) s2 += "P";
		if ((s[i] == 'P') && (s[i+1] == 'S')) s2 += "S";
		if ((s[i] == 'S') && (s[i+1] == 'P')) s2 += "S";
		if ((s[i] == 'S') && (s[i+1] == 'R')) s2 += "R";
	}
	return checkString(s2);
}

string res;

void runTest (int R, int P, int S, string cur)
{
	if ((R == 0) && (P == 0) && (S == 0))
	{
		if (checkString(cur))
		{
			if (cur < res) res = cur;
		}
	}
	else
	{
		if (R) runTest(R-1, P, S, cur + "R");
		if (P) runTest(R, P-1, S, cur + "P");
		if (S) runTest(R, P, S-1, cur + "S");
	}
}

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int N, R, P, S;
		scanf("%d %d %d %d",&N,&R,&P,&S);
		res = "Z";
		runTest(R, P, S, "");
		cout << "Case #" << (iT+1) << ": ";
		if (res == "Z") cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	return 0;
}
