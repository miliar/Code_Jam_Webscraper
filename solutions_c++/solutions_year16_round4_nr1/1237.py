#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T, R, P, S, N;
int num[27];
string solve(char X, int L)
{
	if(L==N)
	{
		num[X-'A']++;
		string s;
		s.push_back(X);
		return s;
	}
	if(X=='R')
	{
		string A = solve('R', L+1);
		string B = solve('S', L+1);
		return min(A, B)+max(A, B);
	}
	if(X=='S')
	{
		string A = solve('S', L+1);
		string B = solve('P', L+1);
		return min(A, B)+max(A, B);
	}
	if(X=='P')
	{
		string A = solve('P', L+1);
		string B = solve('R', L+1);
		return min(A, B)+max(A, B);
	}
}
int main()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		num['R'-'A']=0;
		num['P'-'A']=0;
		num['S'-'A']=0;
		string ANS="IMPOSSIBLE";
		bool imp=true;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		string A = solve('P', 0);
		D("%s %d %d %d\n", A.c_str(), num['R'-'A'], num['P'-'A'],num['S'-'A']);
		if(num['R'-'A']==R && num['P'-'A']==P && num['S'-'A']==S)
		{
			if(imp)
			{
				ANS = A;
				imp = false;
			}
			else ANS = min(A, ANS);
		}
		num['R'-'A']=0;
		num['P'-'A']=0;
		num['S'-'A']=0;
		A = solve('S', 0);
		D("%s %d %d %d\n", A.c_str(), num['R'-'A'], num['P'-'A'],num['S'-'A']);
		if(num['R'-'A']==R && num['P'-'A']==P && num['S'-'A']==S)
		{
			if(imp)
			{
				ANS = A;
				imp = false;
			}
			else ANS = min(A, ANS);
		}
		num['R'-'A']=0;
		num['P'-'A']=0;
		num['S'-'A']=0;
		A = solve('R', 0);
		D("%s %d %d %d\n", A.c_str(), num['R'-'A'], num['P'-'A'],num['S'-'A']);
		if(num['R'-'A']==R && num['P'-'A']==P && num['S'-'A']==S)
		{
			if(imp)
			{
				ANS = A;
				imp = false;
			}
			else ANS = min(A, ANS);
		}
		printf("Case #%d: %s\n", t, ANS.c_str());
	}
}