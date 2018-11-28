#include <bits/stdc++.h>
using namespace std;

string P[20]; //paper
string R[20]; //rock
string S[20]; //scissors
bool dupa;
void prepare()
{
	P[0] = "P";
	R[0] = "R";
	S[0] = "S";
	for(int i = 1; i < 15; ++i)
	{
		if(P[i-1] < R[i-1])
			P[i] = P[i-1] + R[i-1];
		else
			P[i] = R[i-1] + P[i-1];
		if(S[i-1] < R[i-1])
			R[i] = S[i-1] + R[i-1];
		else
			R[i] = R[i-1] + S[i-1];
		if(P[i-1] < S[i-1])
			S[i] = P[i-1] + S[i-1];
		else
			S[i] = S[i-1] + P[i-1];
	}
	//debug
	/*
	for(int i = 0; i < 6; ++i)
	{
		cout << i << endl << S[i] << endl << R[i] << endl << P[i] << endl;
	}*/
	
}
int ile(const string& X, char c)
{
	int res = 0;
	for(int i = 0; i < X.size(); ++i)
		if(X[i] == c)
			++res;
	//printf("res = %d %s\n", res, X.c_str());
	return res;
}
void solver()
{
	if(dupa == false)
	{
		prepare();
		dupa = true;
	}
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	//--n;
	string tmp;
#define ZGADZA(x) (p == ile(x, 'P') && r == ile(x, 'R') && s == ile(x, 'S'))
	if(ZGADZA(P[n]) && (P[n] < tmp || tmp.size() == 0)) tmp = P[n];
	if(ZGADZA(R[n]) && (R[n] < tmp || tmp.size() == 0)) tmp = R[n];
	if(ZGADZA(S[n]) && (S[n] < tmp || tmp.size() == 0)) tmp = S[n];
	if(tmp.size() == 0)
		puts("IMPOSSIBLE");
	else
		puts(tmp.c_str());
	
}
int main()
{
	ios_base::sync_with_stdio(0);
	//prepare();
	//return 0;
	//solver();
	//return 0;
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solver();
		//puts("");
	}
	
	
	return 0;
}
