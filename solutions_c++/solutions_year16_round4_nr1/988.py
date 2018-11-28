#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
typedef pair<int,int> ii;

#define fi first
#define se second
#define pb push_back
#define mp make_pair

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;

vector<string> vec[13];

bool ok(string x, string y)
{
	string z = x + y;
	string tmp = z;
	while(tmp.size() >= 2)
	{
		string tmp2;
		for(int i = 0; i < tmp.size()/2; i++)
		{
			tmp2.append(" ");
			if(tmp[2*i] == tmp[2*i + 1]) return false;
			if(tmp[2*i] == 'P' && tmp[2*i + 1] == 'S') tmp2[i] = 'S';
			if(tmp[2*i] == 'S' && tmp[2*i + 1] == 'P') tmp2[i] = 'S';
			if(tmp[2*i] == 'R' && tmp[2*i + 1] == 'S') tmp2[i] = 'R';
			if(tmp[2*i] == 'S' && tmp[2*i + 1] == 'R') tmp2[i] = 'R';
			if(tmp[2*i] == 'P' && tmp[2*i + 1] == 'R') tmp2[i] = 'P';
			if(tmp[2*i] == 'R' && tmp[2*i + 1] == 'P') tmp2[i] = 'P';
		}
		tmp = tmp2;
	}
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A-large (3).in", "r", stdin);
	//freopen("A-small-attempt0 (2).in", "r", stdin);
	freopen("GCJ20162A.out", "w", stdout);
	int t; cin >> t;
	int T = 0;
	vec[0].pb("P"); vec[0].pb("R"); vec[0].pb("S");
	for(int i = 1; i < 13; i++)
	{
		for(int j = 0; j < vec[i-1].size(); j++)
		{
			for(int k = j; k < vec[i-1].size(); k++)
			{
				//cout << j << ' ' << k << endl;
				if(ok(vec[i-1][j], vec[i-1][k]))
				{
					vec[i].pb(vec[i-1][j] + vec[i-1][k]);
					//cout << vec[i-1][j] + vec[i-1][k] << endl;
				}
			}
		}
		sort(vec[i].begin(), vec[i].end());
	}
	while(t--)
	{
		T++;
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << T << ": ";
		string tmp = "";
		for(int i = 0; i < vec[n].size(); i++)
		{
			int rr, pp, ss;
			rr = 0; pp = 0; ss = 0;
			for(int j = 0; j < vec[n][i].length(); j++)
			{
				if(vec[n][i][j] == 'R') rr++;
				if(vec[n][i][j] == 'S') ss++;
				if(vec[n][i][j] == 'P') pp++;
				if(rr > r || pp > p || ss > s)
				{
					break;
				}
			}
			if(rr == r && pp == p && ss == s)
			{
				tmp = vec[n][i];
				break;
			}
		}
		if(tmp == "") cout << "IMPOSSIBLE";
		else cout << tmp;
		cout << '\n';
	}
	return 0;
}
