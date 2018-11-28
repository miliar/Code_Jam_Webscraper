#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <map>

std::map<std::string,int> M;

int n;
int a[21][1005];
int cnt[21];

bool u[21];

int ans;

inline int calc(int n)
{
	static bool f1[10005],f2[10005];
	memset(f1,0,sizeof(f1));
	memset(f2,0,sizeof(f2));
	int i,j;
	int ret=0;
	for (i=1;i<=n;i++) {
		if (!u[i]) {
			for (j=1;j<=cnt[i];j++) {
				int x=a[i][j];
				if (f1[x]) continue;
				if (f2[x]) ++ret;
				f1[x]=1;
			}
		} else {
			for (j=1;j<=cnt[i];j++) {
				int x=a[i][j];
				if (f2[x]) continue;
				if (f1[x]) ++ret;
				f2[x]=1;
			}
		}
	}
	return ret;
}

inline void dfs(int x)
{
	if (x>n) {
		ans=std::min(ans,calc(n));
		return;
	}
	if (calc(x-1)>=ans) return;
	u[x]=1;
	dfs(x+1);
	u[x]=0;
	dfs(x+1);
}

inline void solve()
{
	M.clear();
	scanf("%d\n",&n);
	int i;
	int _cnt=0;
	u[2]=1;
	memset(cnt,0,sizeof(cnt));
	for (i=1;i<=n;i++) {
		std::string s;
		std::getline(std::cin,s);
		std::stringstream ss;
		ss<<s;
		std::string tmp;
		while (1) {
			tmp="";
			ss>>tmp;
			if (tmp=="") break;
			if (!M[tmp]) M[tmp]=++_cnt;
			a[i][++cnt[i]]=M[tmp];
		}
	}
	ans=100000;
	dfs(3);
	printf("%d\n",ans);
}

int main()
{
	int T;
	scanf("%d\n",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}