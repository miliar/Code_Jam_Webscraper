

#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------



vector<int> ans;

bool dfs(vector<int> tmp, int L, int leftS) {
	if(leftS == 0) {
		ans = tmp;
		return true;
	}
	for(int i=L;i>=2;i--) if(i<=leftS){
		tmp.push_back(i);
		if(dfs(tmp, i, leftS-i))
			return true;
		tmp.pop_back();
	}
	return false;
}

vector<int> get(int maxL, int S) {
	ans.clear();
	for(int i=maxL;i>=2;i--) if(S>=2*i){
		vector<int> tmp(2, i);
		if(dfs(tmp, i, S-2*i))
			return ans;
	}
	return ans;
}



int main() {
	freopen("F:/TDDOWNLOAD/C-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/C-large.out", "w", stdout);
	
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int R, C, M;
		cin>>R>>C>>M;
		vector<string> mp(R, string(C, '*'));
		vector<int> v;

		if(R*C-M == 1) {
			mp[0][0] = 'c';
			goto success;
		}
		
		if(R==1 || C==1) {
			for(int i=0, cnt = 1;i<R;i++) for(int j=0;j<C;j++) {
				if(cnt<=R*C-M) {
					mp[i][j] = '.';
				}
				cnt++;
			}
			mp[0][0] = 'c';
			goto success;
		}

		v = get(R, R*C-M);
		if(v.size() && v.size() <= C) {
			for(int j=0;j<(int)v.size();j++) {
				for(int i=0;i<v[j];i++) mp[i][j] = '.';
			}
			mp[0][0] = 'c';
			goto success;
		}
		
		v = get(C, R*C-M);
		if(v.size() && v.size() <= R) {
			for(int i=0;i<(int)v.size();i++) {
				for(int j=0;j<v[i];j++) mp[i][j] = '.';
			}
			mp[0][0] = 'c';
			goto success;
		}

failure:;
		printf("Case #%d:\n", te);
		puts("Impossible");
		continue;

success:;
		printf("Case #%d:\n", te);
		for(int i=0;i<(int)mp.size();i++) cout<<mp[i]<<endl;
		continue;

	}
}








