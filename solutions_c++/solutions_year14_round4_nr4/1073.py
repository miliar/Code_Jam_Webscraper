#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
#define MAX_L 10

int res, cnt, m, n;
int gt[MAX_L];
bool flag[MAX_L];
string s[MAX_L];
vector<string> v;

int qry()
{
	int tt = 0;
	for(int i = 1; i <= n; ++i) {
		v.clear();
		for(int j = 1; j <= m; ++j) {
			if(gt[j] == i)
				v.push_back(s[j]);
		}
		sort(v.begin(),v.end());
		tt += v[0].size();
		for(int j = 1; j < v.size(); ++j) {
			int flag = 0;
			for(int k = 0; k < v[j].size() && k < v[j-1].size(); k++) {
				if(v[j][k] != v[j-1][k])
					break;
				else
					flag++;
			}
			tt += v[j].size()-flag;
		}
	}
	if(tt > res) {
		cnt = 1;
		res = tt;
	}
	else if(tt==res)
		cnt++;
}

int dfs(int p) {
	if(p > m) {
		memset(flag,0,sizeof(flag));
		for(int i = 1; i <= m; ++i)
			flag[gt[i]] = 1;
		for(int i = 1; i <= n; ++i)
			if(!flag[i])
				return 0;
		qry();
		return 0;
	}
	for(int i = 1; i <= n; ++i) {
		gt[p] = i;
		dfs(p+1);
	}
}

int main() {
	int t,cs=0;
	cin>>t;
	while(t--) {
		cin>>m>>n;
		for(int i = 1; i <= m; ++i)
			cin>>s[i];
		cnt = 0;
		res = 0;
		dfs(1);
		printf("Case #%d: %d %d\n",++cs,res+n,cnt);
	}
}
 