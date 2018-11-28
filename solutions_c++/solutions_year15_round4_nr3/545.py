#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <cmath> 
#include <cstring> 
#include <queue>
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define PRIME1 31415 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef vector<vector<int> > vvi; 
//------------------------------------------------------------ 
#define y1 asdf
#define y2 asdqwer
const int N = 3000;
map <string, int> vol;
int was[N];
int v[N];
int n;
vvi pr;
void solve()
{
	cin >> n;
	vol.clear();
	memset(was, 0, sizeof was);
	memset(v, 0, sizeof v);
	pr.clear();
	string st;
	pr.resize(n);
	getline(cin, st);
	getline(cin, st);
	
	for(int i = 0; i < st.size(); ++i)
	{
		string t = "";
		while(st[i] != ' ' && i < st.size())
		{
			t += st[i];
			i++;
		}
		if (vol.find(t) == vol.end())
		{
			int k = vol.size();
			vol[t] = k;
			v[k] = 2;
		}
		pr[0].push_back(vol[t]);
	}
	int de = 0;
	getline(cin, st);
	for(int i = 0; i < st.size(); ++i)
	{
		string t = "";
		while(st[i] != ' ' && i < st.size())
		{
			t += st[i];
			i++;
		}
		if (vol.find(t) == vol.end())
		{
			int k = vol.size();
			vol[t] = k;
			v[k] = 1;
		}
		int k = vol[t];
		if (v[k] == 2)
		{
			v[k] = 3;
			de++;
		}
		pr[1].push_back(k);
		t = "";
	}
	for(int j = 2; j < n; ++j)
	{
		getline(cin, st);
		for(int i = 0; i < st.size(); ++i)
		{
			string t = "";
			while(st[i] != ' ' && i < st.size())
			{
				t += st[i];
				i++;
			}
			//cerr << t << 's';
			if (vol.find(t) == vol.end())
			{
				int k = vol.size();
				vol[t] = k;
			}
			pr[j].push_back(vol[t]);
		}
	}

	int bans = 3000;
	for(int i = 0; i < (1 << (n - 2)); ++i)
	{
		int ans = 0;
		for(int j = 2; j < n; ++j)
			for(int r = 0; r < pr[j].size(); ++r)
				was[pr[j][r]] = 0;

		for(int j = 0; j < n - 2; ++j)
		{
			int q = 0;
			if ((1ll << j) & i)
				q = 1;
			else
				q = 2;
			//cerr << q << ' ';
			for(int r = 0; r < pr[j + 2].size(); ++r)
			{
				int ke = pr[j + 2][r];
				if (q & was[ke])
					continue;
				if (q & v[ke])
					continue;

				if (v[ke])
				{
					was[ke] = 3;
					ans++;
					continue;
				}

				if(was[ke])
				{
					was[ke] = 3;
					ans++;
				}
				else
					was[ke] = q;

			}
		}
		bans = min(bans, de + ans);
	}
	
	cout << bans;
}

int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	string st;
	getline(cin, st);
	
	for(int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}