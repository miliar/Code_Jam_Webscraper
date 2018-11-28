#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
using namespace std;
typedef long long ll;
typedef double db;
const db pi=acos(-1);
void gn(int &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
void gn(ll &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
const int mo=1000000007;
int qp(int a,ll b){int ans=1;do{if(b&1)ans=1ll*ans*a%mo;a=1ll*a*a%mo;}while(b>>=1);return ans;}
int n;
db v,x;
db r[111],c[111];
#define eps 1e-14

db det(db a,db b,db c,db d){
	return a*d-b*c;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
	int tes;scanf("%d",&tes);
	for (int tt=1;tt<=tes;tt++){
		scanf("%d",&n);
		printf("Case #%d: ",tt);
		double vv,xx;
		scanf("%lf%lf",&vv,&xx);
		v=vv,x=xx;
		for (int i=1;i<=n;i++)scanf("%lf%lf",&vv,&xx),r[i]=vv,c[i]=xx;
		if(n==2){
			if(fabs(c[2]-c[1])<eps){
				r[1]=r[1]+r[2];
				n=1;
			}
		}
		if(n==2){
			db r1=c[1],r2=c[2],rr=x;
			if(rr<r1 && rr<r2 || rr>r1 && rr>r2){
				printf("IMPOSSIBLE\n");
				continue;
			}
			else{
				db x1=det(v,r[2],x*v,c[2]*r[2])/det(r[1],r[2],c[1]*r[1],c[2]*r[2]);
				db x2=det(r[1],v,c[1]*r[1],x*v)/det(r[1],r[2],c[1]*r[1],c[2]*r[2]);
				printf("%.16lf\n",double(max(x1,x2)));
			}
		}
		else if(n==1){
			db r1=c[1],rr=x;
			if(fabs(r1-rr)>eps){
				printf("IMPOSSIBLE\n");
				continue;
			}
			else printf("%.16lf\n",double(v/r[1]));
		}


	}
	return 0;
}



