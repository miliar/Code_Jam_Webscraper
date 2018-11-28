#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MOD 1000002013
#define LL long long

using namespace std;

struct node {
	int posi;
	int num;

	node() {};
	node(int _posi,int _num):posi(_posi),num(_num) {};
};

int tt;
int n,m;
node a[2000];
LL ans1,ans2;
int cnt;
int top;
int st[2000][2];

int getans(int st,int ed,int num) {
	LL p=ed-st;
	p=(LL)(n+n-p+1)*(LL)p/2 % MOD;
	p=p*(LL)num%MOD;
	return (int)p;
}

bool cmp(const node &a,const node &b) {
	if (a.posi!=b.posi) return a.posi<b.posi;
	else return a.num>0;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d",&n,&m);
		ans1=0,ans2=0;
		cnt=0;
		for (int i=0;i<m;++i) {
			int st,ed,num;
			scanf("%d%d%d",&st,&ed,&num);
			ans1+=getans(st,ed,num);
			ans1%=MOD;
			a[cnt++]=node(st,num);
			a[cnt++]=node(ed,-num);
		}
		sort(a,a+cnt,cmp);
		top=0;
		for (int i=0;i<cnt;++i)
			if (a[i].num>0) {
				st[top][0]=a[i].posi;
				st[top][1]=a[i].num;
				top++;
			} else {
				int res=abs(a[i].num);
				while (res>0) {
					int off=min(st[top-1][1],res);
					ans2+=getans(st[top-1][0],a[i].posi,off);
					ans2%=MOD;
					res-=off;
					st[top-1][1]-=off;
					if (st[top-1][1]==0) top--;
				}
			}
		ans1-=ans2;
		if (ans1<0) ans1+=MOD;
		printf("Case #%d: %d\n",ii,(int)ans1);
	}
}
