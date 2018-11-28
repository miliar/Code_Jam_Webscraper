#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include<cstdlib>
#include<queue>
using namespace std;

#define pb push_back
#define mp make_pair
#define sc second
#define ft first

#define FOR(i,N) for (int i=1; i<=N; i++)
#define REP(i,l,r) for (int i=l; i<=r; i++)

#define INF ~0U>>1
#define eps 1e-9

int ans[270];
int n, R, P, S;

string solve (string k, int pos)
{
	string ret, A, B;
	if (pos >= (1 << n))
	{
		ans[k[0]]++;
		return k;
	}
	A = solve (k, pos << 1);
	//cout << A << endl;
	string tmp;
	if (k == "R")
	{
		tmp = "S";
	}
	if (k == "P")
	{
		tmp = "R";
	}
	if (k == "S")
	{
		tmp = "P";
	}
	B = solve (tmp, (pos << 1) | 1);
	//cout << B << endl;
	if (A < B) ret = A + B;
	else ret = B + A;
	return ret;
}

void modify (string &ANS, string tmp)
{
	if (ans['R'] != R) return;
	
	if (ans['P'] != P) return;
	
	if (ans['S'] != S) return;
	
	if (ANS.size() == 0) ANS = tmp;
	else if (ANS > tmp) ANS = tmp;
}

int main ()
{
#ifndef ONLINE_JUDGE
#ifndef MEKTPOY
	freopen (".in", "r", stdin);
	freopen (".out", "w", stdout);
#else
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
#endif
#endif
	int T;
	cin >> T;
	for (int test = 1; test <= T; test ++)
	{
		printf ("Case #%d: ", test);
		cin >> n;
		cin >> R >> P >> S;
		string ANS;
		
		memset (ans, 0, sizeof(ans));
		string tmp = solve ("R", 1);
		modify (ANS, tmp);
		
		memset (ans, 0, sizeof(ans));
		tmp = solve ("P", 1);
		modify (ANS, tmp);
		
		memset (ans, 0, sizeof(ans));
		tmp = solve ("S", 1);
		modify (ANS, tmp);
		
		if (ANS.size() == 0)
			puts("IMPOSSIBLE");
		else
			cout << ANS << endl;
	}
	return 0;
}

