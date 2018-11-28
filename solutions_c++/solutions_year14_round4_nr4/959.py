#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;

int serv[100];

int m, n;
vector<string> ss;
vector<vector<string>> ssPrefs;

vector<string> genPrefs(const string& s)
{
	vector<string> ans;
	rep(i,s.size()+1)
		ans.push_back(s.substr(0,i));

	return ans;
}

void insertAllPref(const string& s, set<string>& prefs)
{
	rep(i,s.size()+1)
		prefs.insert(s.substr(0,i));
}

int ans, cnt;

vector< vector<string> > srv;

void brute_force(int i = 0)
{
	if (i == m)
	{
		srv.resize(n);
		rep(j,n)
			srv[j].clear();

		rep(j,m)
			srv[serv[j]].insert(srv[serv[j]].end(), ssPrefs[j].begin(), ssPrefs[j].end());// (ss[j], srv[serv[j]]);

		int cans = 0;
		rep(j,n)
		{
			sort(srv[j].begin(), srv[j].end());
			cans += unique(srv[j].begin(), srv[j].end()) - srv[j].begin();
		}

		if (cans > ans)
		{
			ans = cans;
			cnt = 1;
		}
		else if (cans == ans)
		{
			cnt++;
		}
		return;
	}
	rep(j,n)
	{
		serv[i] = j;
		brute_force(i+1);
	}
}

int main()
{
    ofstream fout("out.txt");
    freopen("in.txt","r",stdin);
	//freopen("debug.txt","w",stdout);

    int t;
    cin >> t;

	rep(tc,t)
	{
		cin >> m >> n;
		ss.resize(m);
		ssPrefs.resize(m);
		rep(i,m)
		{
			cin >> ss[i];
			ssPrefs[i] = genPrefs(ss[i]);
		}

		ans = 0;
		cnt = 0;
		brute_force();

		fout << "Case #" << tc + 1 << ": " << ans << " " << cnt << "\n";
		cout << tc << endl; 
	}

    return 0;
}