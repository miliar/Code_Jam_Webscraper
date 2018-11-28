#include <bits/stdc++.h>
#include "testlib.h"
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second

int n;
int p[105];
string f;	
typedef long double ld;
ld dp[105];

vector<int> kids[105];

ld C[105][105];
int s[105];
void csum(int v)
{
	s[v] = 1;
	for (int to:kids[v])
	{
		csum(to);
		s[v] += s[to];
	}
}

void dfs(int v)
{
	dp[v] = 1;
	int r = s[v] - 1;
	for (int to: kids[v])
	{
		dfs(to);
		dp[v] *= dp[to] * C[r][s[to]];
		r -= s[to];
	}
}


string genrand()
{
	vector<bool> used(n);
	
	string res = "";
	//cerr << "gen" << endl;
	for (int i = 0; i < n; i++)
	{
	//	cerr << "i=" << i << endl;
		vector<ld> prob(n);
		ld v = 1.;
		int rest = n - i;
		for (int k = 0; k < n; k++)
		   if (!used[k] && (p[k] == -1 || used[p[k]]))
		   {
			  v *= dp[k] * C[rest][s[k]];
			  rest -= s[k];
		   }
	//	cerr << "v=" << v << endl;
		for (int j = 0; j < n; j++)
		{
			if (used[j] || (p[j] != -1 && !used[p[j]])) prob[j] = 0;
			else
			{
				prob[j] = v;
				prob[j] /= dp[j] * C[n-i][s[j]];
				int rest0 = n-i-1;
				for (int k : kids[j])
				{
				   prob[j] *= dp[k] * C[rest0][s[k]];
				   rest0 -= s[k];
			   }
			   
			}
		}
		ld s = 0;
		for (int j = 0; j < n; j++) s += prob[j];
		vector<int> q(n+1);
		//for (int j = 0; j < n; j++) cerr << (double)prob[j] << ' ';
		//cerr << endl;
		int A = (int)1e9;
		q[0] = 0;
		for (int j = 1; j <= n; j++)
		   q[j] = q[j-1] + (int)(prob[j-1]/s * (ld)A);
		
		int c = rnd.next(0,q[n]-1);
		int val = -1;
		for (int j = 0; j < n; j++)
		   if (c >= q[j] && c < q[j+1]) val = j;
		assert(val != -1);
		res.pb(f[val]);
		used[val] = 1;
	}
	//cout << endl;
	return res;
}


void solve(int test)
{
	cin >> n;
	for (int i = 0; i < n; i++) kids[i].clear();
	for (int i = 0; i < n; i++) {cin >> p[i]; p[i]--; if (p[i]>=0) kids[p[i]].pb(i);}
	for (int i = 0; i < n; i++)
	   if (p[i] == -1) csum(i);
	for (int i = 0; i < n; i++)
	   if (p[i] == -1) dfs(i);
	cerr << "finished " << test << endl;
	cin >> f;
	int m;
	cin >> m;
	vector<string> word(m);
	for (int i = 0; i < m; i++)
	   cin >> word[i];
	int A = 5000;
	vector<int> cnt(m);
	for (int i = 0; i < A; i++)
	{
		string g = genrand();
		//cout << g << endl;
		for (int j = 0; j < m; j++)
		{
			for (int k = 0; k + (int)word[j].size() <= n; k++)
			   if (g.substr(k, (int)word[j].size()) == word[j])
			   { cnt[j]++;
				 break;
			   }
		}
	}
	cout << "Case #" << test << ": ";
	for (int i = 0; i < m; i++) cout << (double)cnt[i]/A << " \n"[i==m-1];
}


int main()
{
	C[0][0] = 1.;
	for (int i = 1; i < 102; i++)
	{
		C[i][0] = 1.;
		for (int j = 1; j < 102; j++)
		   C[i][j] = C[i-1][j-1] + C[i-1][j];
	}
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; i++)
	{
		solve(i+1);
	}
	return 0;
}
