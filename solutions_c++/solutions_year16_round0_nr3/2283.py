#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;
#define X first
#define Y second



int n,k;

int get(int mask, int C, int mod)
{
	int a = 1;
	for (int i = 0; i < n-2; i++)
	   a = (a * C + ((mask>>i)&1)) % mod;
	a = (a * C + 1) % mod;
	return a;
}

void solve(int test)
{
//	int n, k;
	cin >> n >> k;
	vector<int> ans;
	vector<vector<int> > g;
	//cerr << "!!" << endl;
	for (int mask = 0; mask < (1<<(n-2)); mask++)
	{
		if (mask % 10000 == 0) cerr << mask << endl;
		bool gok = 1;
		vector<int> proof;
		for (int sys = 2; sys <= 10 && gok; sys++)
		{
			bool ok = 0;
			for (int mod = 2; mod <= 100 && !ok; mod++)
			{
				if (get(mask, sys, mod) == 0) {proof.pb(mod); ok = 1;}
			}
			if (!ok) gok = 0;
		}
		if (gok) 
		{
			ans.pb(mask);
			g.pb(proof);
			if (ans.size() == k) break;
		}
	} 
//	cerr << "!!! " << ans.size() << endl;
	cout << "Case #" << test << ":\n";
	for (int i = 0; i < k; i++)
	{
		cout << 1;
		for (int j = 0; j < n-2; j++) cout << ((ans[i]>>j)&1);
		cout << "1 ";
		for (int j = 0; j < (int)g[i].size(); j++) cout << g[i][j] << " \n"[j==(int)g[i].size()-1];
	}
	
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}
