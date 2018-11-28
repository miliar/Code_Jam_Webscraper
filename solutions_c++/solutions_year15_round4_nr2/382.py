#include<bits/stdc++.h>
using namespace std;
typedef double dbl;
int n;
dbl c[128],r[128],l[128],v,x;
const dbl eps=1e-10;
bool ok(dbl t){
	for(int i=0;i<n;++i)l[i]=t*r[i];
	dbl u=v;
	for(int i=0;i<n;++i)if(c[i]==0){
		t=min(u,l[i]);
		u-=t;l[i]-=t;
	}
	if(u<=eps)return true;
	for(int i=0;i<n && u>eps;++i)
		for(int j=i+1;j<n && u>eps;++j)
			if(c[i]*c[j]<0 && l[i]>0 && l[j]>0){
				dbl ci=fabs(c[i]),cj=fabs(c[j]);
				dbl k=min(u/(ci+cj),min(l[j]/ci,l[i]/cj));
				l[i]-=k*cj;
				l[j]-=k*ci;
				u-=k*(ci+cj);
			}
	return u<=eps;
}
int main(){
	int T;
	cin >> T;
	for(int ti=1;ti<=T;++ti){
		cin >> n >> v >> x;
		bool b[2]={false,false};
		for(int i=0;i<n;++i){
			cin >> r[i] >> c[i];
			b[0]|=(c[i]<=x);
			b[1]|=(c[i]>=x);
			c[i]-=x;
		}
		printf("Case #%d: ",ti);
		if(!b[0] || !b[1]){
			puts("IMPOSSIBLE");
			continue;
		}
		dbl l=0,r=1;
		for(;!ok(r) && r<1e100;l=r,r*=2);
		if(r>1e100){
			puts("IMPOSSIBLE");
			continue;
		}
		for(int tm=100;tm--;){
			dbl m=ldexp(l+r,-1);
			if(ok(m))r=m;else l=m;
		}
		printf("%.12lf\n",l);
	}
}
