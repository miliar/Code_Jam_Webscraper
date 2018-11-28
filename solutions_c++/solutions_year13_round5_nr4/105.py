#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int tt;
string s;
int n;
double f[1 << 20];
double p[1 << 20];
int a[20];

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii) {
		cin >> s;
		n=s.size();
		reverse(s.begin(),s.end());
		memset(f,0,sizeof(f));
		memset(p,0,sizeof(p));
		int st=0;
		for (int i=0;i<n;++i)
			if (s[i]=='X') st+=(1<<i);
		p[st]=1;
		for (int i=0;i<(1 << n);++i) {
			for (int j=0;j<n;++j)
				if ((i >> j)&1) a[j]=1;
				else a[j]=0;
			int pre=-1;
			for (int j=0;j<n;++j)
				if (a[j]==0) pre=j;
			if (pre==-1) continue;
			int now=pre;
			for (int j=pre;j<pre+n;++j) {
				if (a[j%n]==0) now=j;
				int k=now%n;
				p[i|(1<<k)]+=p[i]/n;
				f[i|(1<<k)]+=f[i]/n+p[i]/n*(n-(j-now));
			}
		}
		//printf("%.10lf %.10lf\n",p[3],p[6]);
		//printf("%.10lf %.10lf\n",f[3],f[6]);
		printf("Case #%d: %.10lf\n",ii,f[(1<<n)-1]);
	}
}



