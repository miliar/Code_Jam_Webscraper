#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
using namespace std;

 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef long long ll;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 
 #define MOD 1000000007
int N,M;
vector< vector<string> > list;
map <int,vector <string> > m;
map <int,ll> ret;
int MAX;

int check ()
{
	for (int i=0 ; i<sz(list) ; i++) if (list[i].empty()) return -1;
	
	int ans = 0;
	
	for (int i=0 ; i<sz(list) ; i++)
	{
		set <string> S;
		for (int j=0 ; j<sz(list[i]) ; j++) S.insert(list[i][j]);
		ans += sz(S);
	}
	
	return ans;
}

void solve (int ind)
{
	if (ind == N)
	{
		int ans = check();
		ret[ans]++;
		MAX = max(MAX,ans);
		return ;
	}
	
	for (int i=0 ; i<M ; i++)
	{
		vector <string> vs = list[i];
		vector <string> v = m[ind];
		for (int j=0 ; j<sz(v) ; j++)
		{
			list[i].pb(v[j]);
		}
		
		solve (ind+1);
		list[i] = vs;
	}
}

int main ()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	
	while (TC--)
	{
		cin >> N >> M;
		m.clear();
		ret.clear();
		list.clear();
		list.resize(M);
		MAX = -1;
		
		for (int i=0 ; i<N ; i++)
		{
			string s;
			cin >> s;
			string cur="";
			vector <string> v;
			
			for (int j=0 ; j<sz(s) ; j++)
			{
				cur += s[j];
				v.pb(cur);
			}
			
			m[i] = v;
		}
		
		solve(0);
		
		printf("Case #%d: %d %lld\n",CC++,MAX+M,ret[MAX]%MOD);
	}
}
