#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#define mp make_pair
#define fi first
#define se second

using namespace std;

int tt,n,pn;
int f[26];
int mask[26];
int cnta[26],cntb[26];
int ans,pans;
char g[26][26];
int p,q;
int best[65536][26][26];
pair<int,int> now[65536];

inline int sqr(int x) {
	return x*x;
}

int find(int x) {
	if (x!=f[x]) f[x]=find(f[x]);
	return f[x];
}

void connect(int x,int y) {
	x=find(x),y=find(y);
	f[x]=y;
}

int search(int mask,int p,int q) {
	if (mask==0) {
		if (p!=q) return 100000;
		return p;
	}
	if (best[mask][p][q]!=-1) return best[mask][p][q];
	best[mask][p][q]=100000;
	int tmp=mask;
	while (tmp>0) {
		int pp=now[tmp].fi,qq=now[tmp].se;
		int res=sqr(max(pp,qq));
		if (pp>=qq) {
			if (q>=pp-qq) res+=search(mask-tmp,p,q-(pp-qq));
			else res+=100000;
		} else {
			if (p>=qq-pp) res+=search(mask-tmp,p-(qq-pp),q);
			else res+=100000;
		}
		best[mask][p][q]=min(best[mask][p][q],res);
		tmp=(tmp-1)&mask;
	}
	return best[mask][p][q];
}

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	scanf("%d\n",&tt);

	for (int ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j)
				scanf("%c",&g[i][j]);
			scanf("\n");
		}
		ans=0;
		for (int i=0;i<n;++i)
			f[i]=i;
		memset(mask,0,sizeof(mask));
		for (int i=0;i<n;++i) {
			int cur=-1;
			for (int j=0;j<n;++j) 
				if (g[i][j]=='1') {
					if (cur==-1) cur=j;
					mask[j]|=(1<<i);
					ans--;
					connect(cur,j);
				}
		}
		memset(cnta,0,sizeof(cnta));
		memset(cntb,0,sizeof(cntb));
		for (int i=0;i<n;++i) {
			mask[find(i)]|=mask[i];
			cnta[find(i)]++;
		}

		p=0,q=n;
		
		vector<pair<int,int> > cur;
		cur.clear();
		for (int i=0;i<n;++i)
			if (find(i)==i) {
				cntb[i]=__builtin_popcount(mask[i]);
				q-=cntb[i];
				if (cnta[i]==cntb[i]) ans+=cnta[i]*cnta[i];
				else if (cntb[i]==0) p++;
				else cur.push_back(mp(cnta[i],cntb[i]));
			}

		pn=cur.size();
		//printf("%d %d %d\n",pn,p,q);
		//for (int i=0;i<pn;++i)
		//	printf("%d %d\n",cur[i].fi,cur[i].se);
		for (int i=0;i<1<<pn;++i)
			for (int j=0;j<n;++j)
				for (int k=0;k<n;++k)
					best[i][j][k]=-1;
		for (int i=0;i<1<<pn;++i) {
			now[i].fi=0,now[i].se=0;
			for (int j=0;j<pn;++j)
				if ((i>>j)&1) now[i].fi+=cur[j].fi,now[i].se+=cur[j].se;
		}
		ans+=search((1<<pn)-1,p,q);

		printf("Case #%d: %d\n",ii,ans);
		fflush(stdout);
	}
}