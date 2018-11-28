#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;++a)
#define per(a,b,c) for(int a=b;a>=c;--a)
#define X first
#define Y second
#define PII pair<int,int>
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define pb push_back
#define mp make_pair

typedef long long ll;

void read(int &x){
	char cc=getchar();
	for	(;cc<'0' || cc>'9';cc=getchar());
	for	(x=0;cc>='0' && cc<='9';cc=getchar())	x=x*10+cc-'0';
}

int n,TT;
long double v,x,tar;
long double a[111],b[111],tak[111];
const long double eps=1e-8;

bool check(long double lim){
	long double sum,ss;
	sum=ss=0;
	rep(i,1,n)	tak[i]=0;
	rep(i,1,n)
		if	(lim*b[i]+sum>tar+eps){
			tak[i]=(tar-sum)/b[i];
			break;
		}
		else	tak[i]=lim,sum+=tak[i]*b[i];
	rep(i,1,n)	ss+=a[i]*tak[i];
	if	(ss>v+eps)	return	0;
	
	sum=ss=0;
	rep(i,1,n)	tak[i]=0;
	per(i,n,1)
		if	(lim*b[i]+sum>tar+eps){
			tak[i]=(tar-sum)/b[i],sum=tar;
			break;
		}
		else	tak[i]=lim,sum+=tak[i]*b[i];
	rep(i,1,n)	ss+=a[i]*tak[i];
	if	(ss+eps<v)	return	0;
	return	1;
}

int main(){
	//freopen("c.in","r",stdin);freopen("c.txt","w",stdout);
	scanf("%d",&TT);
	rep(T,1,TT){
		cin >>n >>v >>x;
		tar=v*x;
		long double l=0,r=0,mid;
		rep(i,1,n){
			cin >>a[i] >>b[i];
			b[i]*=a[i];
			r=max(r,v/a[i]);
		}
		rep(i,1,n)	rep(j,i+1,n)
			if	(a[i]/b[i]>a[j]/b[j]){
				swap(a[i],a[j]);
				swap(b[i],b[j]);
			}
		if	(!check(r+1)){
			printf("Case #%d: IMPOSSIBLE\n",T);
			continue;
		}
		while	(r-l>1e-14){
			mid=(r+l)/2;
			if	(check(mid))	r=mid;
			else	l=mid;
		}
		printf("Case #%d: %.8lf\n",T,double(l));
		//printf("%d %.8lf %.8lf\n",n,double(v),double(x));
	}
}
