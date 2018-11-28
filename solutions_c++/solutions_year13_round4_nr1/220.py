#include<stdio.h>
#include<algorithm>

typedef long long int lnt;
typedef double dou;
using namespace std;
lnt mod=1000002013;
lnt n,m;
lnt f(lnt d){
	return (n+n-d+1)*d/2%mod;
	}
typedef struct{lnt p,x;}ele;
#include<vector>
ele e[4024];

int cmp(ele a,ele b){return a.x<b.x||a.x==b.x&&a.p>b.p;}
ele h[201200];
lnt top;
void truli(int uuu){
	scanf("%I64d %I64d",&n,&m);
	lnt total=0;
	for(int i=0;i<m;i++){
		lnt ff,t,p;
		scanf("%I64d %I64d %I64d",&ff,&t,&p);
		total=(total+p*f(t-ff)%mod)%mod;
		e[i+i  ]=(ele){ p,ff};
		e[i+i+1]=(ele){-p,t};
		}
	m*=2;
	sort(e,e+m,cmp);
	top=0;
	lnt ans=0;
	for(int i=0;i<m;i++){
		if(e[i].p>=0){
			h[top++]=e[i];
			continue;
			}
		e[i].p*=-1;
		for(;e[i].p;){
			lnt d=min(h[top-1].p,e[i].p);
			ans=(ans+d*f(e[i].x-h[top-1].x)%mod)%mod;
			h[top-1].p-=d;
			e[i].p-=d;
			for(;top&&h[top-1].p==0;top--);
			}
		}
	printf("Case #%d: %I64d\n",uuu,(total-ans+mod)%mod);
	}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("PA-Bout.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)
		truli(ti);
	
	return 0;
	}
