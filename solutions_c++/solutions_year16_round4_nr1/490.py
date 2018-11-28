#include <bits/stdc++.h>
using namespace std;

string best[256][13];
char winner;

string solve(int R, int P, int S)
{
	int n = R + P + S;
	if(n == 1)
	{
		if(R == 1) winner = 'R';
		if(P == 1) winner = 'P';
		if(S == 1) winner = 'S';
		return "";
	}
	if(R > n/2 || P > n/2 || S > n/2) return "";
	int nR = n/2 - P;
	int nS = n/2 - R;
	int nP = n/2 - S;
	string s = solve(nR, nP, nS);
	string ret;
	for(int i = 0; i < s.length(); i++)
		if(s[i] == 'R')
			ret += "RS";
		else if(s[i] == 'P')
			ret += "PR";
		else
			ret += "PS";
	return ret;
}

string comb(string a, string b)
{
	string ret1 = a + b;
	string ret2 = b + a;
	if(ret1 < ret2) return ret1;
	return ret2;
}

void solve()
{
	int n, P, R, S;
	cin >> n >> R >> P >> S;
	winner = 0;
	string t = solve(R, P, S);
	if(winner == 0) cout << "IMPOSSIBLE" << endl;
	else cout << best[winner][n] << endl;
}



int MAIN()
{
	best['P'][0] = "P";
	best['S'][0] = "S";
	best['R'][0] = "R";
	for(int i = 1; i <= 12; i++)
	{
		best['P'][i] = comb(best['P'][i-1], best['R'][i-1]);
		best['S'][i] = comb(best['S'][i-1], best['P'][i-1]);
		best['R'][i] = comb(best['R'][i-1], best['S'][i-1]);
	}

	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	return ret;
}
