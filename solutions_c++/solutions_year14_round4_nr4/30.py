#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int m, n;


int nxt[200100][27];
int df[200100];
int nv;


const long long MOD = 1000000007;

long long C[110][110];
long long FACT[110];

void Load()
{
	cin >> m >> n;
	string s;
	memset(nxt, -1, sizeof(nxt));
	nv = 1;
	for (int i = 0; i < m; i++) {
		cin >> s;
//		cerr << s << "\n";
		int cur = 0;
		for (int j = 0; j < (int)s.size(); j++) {
			int c = (int)s[j] - (int)'A';
			if (nxt[cur][c] == -1) {
				nxt[cur][c] = nv++;
			}
			cur = nxt[cur][c];
//			cerr << cur << ' ';
		}
//		cerr << "\n";
		nxt[cur][26] = nv++; //addng extra symbol at the end;
	}
}

vector <int> A;
int B;
int N;

long long dp[110][30];

long long f(int b, int n) {
	if (n == 0) {
		if (b == 0) return 1;
		else return 0;
	}
	if (dp[b][n] != -1) 
		return dp[b][n];
	
	long long ans = 0;
	for (int i = b; i >= 0; i--) {
		int j = A[n-1] - (b-i);
		if (j < 0) break;
		long long cur = 1;
		cur = C[b][i];
		cur = (cur * f(i, n-1)) % MOD;
		cur = (cur * C[i][j]) % MOD;
//		cur = (cur * FACT[j]) % MOD;		
		ans = (ans + cur) % MOD;
	}

	dp[b][n] = ans;
	return ans;
}


long long Calc(int b, vector<int> &a) {
	if (a.size() == 0)
		a.push_back(1);

	cerr << b << "\n";
	for (int i = 0; i < (int)a.size(); i++)
		cerr << a[i] << ' ';
	cerr << "\n";

	int n = a.size();
	A.clear();
	A.insert(A.begin(), a.begin(), a.end());
	B = b;
	N = n;
	memset(dp, -1, sizeof(dp));
	long long ans = f(b, n);
	cerr << "ans = " << ans << "\n";
	return ans;
}


void Solve()
{
	int i, j;
	long long ans = 1;
	int maxvers = 0;
	for (i = nv-1; i >= 0; i--) {
		int cur = 0;
		vector < int > chlds;
		//cerr << "ver " << i << "\n";
		for (j = 0; j < 27; j++) {
			if (nxt[i][j] != -1) {
				cur+=df[nxt[i][j]];
				chlds.push_back(df[nxt[i][j]]);
				//cerr << df[nxt[i][j]] << " ";
			}
		}

		if (cur > n) cur = n;
		if (cur == 0) cur = 1;
		//cerr << "\ndf " << cur << "\n";
		maxvers += cur;

		df[i] = cur;
		if (chlds.size() > 0);
		ans *= Calc(cur, chlds);
		ans %= MOD;
	}
	if ( df[0] < n )
		ans = ans * C[n][df[0]] % MOD;
	cout << maxvers - m << ' ' << ans << "\n";
}


void CalcC()
{
	int i, j;
	C[0][0] = 1;
	for (i = 1; i < 110; i++) {
		C[i][0] = 1;
		for (j = 1; j <= i; j++) {
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
		}
	}
	FACT[0] = 1;
	for (i = 1; i < 110; i++)
		FACT[i] = (FACT[i-1] * i) % MOD;
}



int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);


	CalcC();

	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
