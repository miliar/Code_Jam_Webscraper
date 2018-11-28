#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

const int MOD = 1000002013;
int a[2000][2];
int ans,should;
int n,m,p;
map <int,int> c;


int cal(int x,int y,int z) {
	long long ans;
	ans=y-x;
	ans=((long long)2*n+1-ans)*ans/2;
	ans=ans*z;
	ans=ans%MOD;
	return ans;
}

void push(int i,int j) {
	a[p][0]=i;
	a[p][1]=j;
	p++;
}

void pop(int i,int j) {
	while (j) {
		if (a[p-1][1]<=j) {
			ans=(ans+cal(a[p-1][0],i,a[p-1][1]))%MOD;
			j-=a[p-1][1];
			p--;
		} else {
			ans=(ans+cal(a[p-1][0],i,j))%MOD;
			a[p-1][1]-=j;
			j=0;
		}
	}
}

int main() {
	int t,tt,i,x,y,z;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		c.clear();
		ans=0;
		should=0;
		p=0;
		scanf("%d%d",&n,&m);
		for (i=1;i<=m;i++) {
			scanf("%d%d%d",&x,&y,&z);
			c[x]+=z;
			c[y]-=z;
			should=(should+cal(x,y,z))%MOD;
		}
		for (map<int,int>::iterator i=c.begin();i!=c.end();i++) {
			if (i->second>0) {
				push(i->first,i->second);
			} else if (i->second<0) {
				pop(i->first,-(i->second));
			}
		}
		//printf("%d %d\n",should,ans);
		ans=(should-ans)%MOD;
		ans=(ans+MOD)%MOD;
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
