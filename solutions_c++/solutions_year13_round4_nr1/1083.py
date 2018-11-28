#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <bitset>
#include <vector>
#include <cstdio>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define Max(x,y) x>y?x:y
#define Min(x,y) x<y?x:y
#define LL long long
using namespace std;
LL T,N,M,res,ans,len,l,r,t;
class rec{public:LL l,r,t;}P[1000010];
bool cmp(const rec&a,const rec&b){return a.l<b.l||(a.l==b.l&&a.r>b.r);}
int main(){
	freopen("A.in","r",stdin);
	freopen("A_.out","w",stdout);
	scanf("%I64d",&T);
	for (LL tt=1;tt<=T;tt++){
		scanf("%I64d%I64d",&N,&M);
		len=0;
		for (LL i=1;i<=M;i++){
			scanf("%I64d%I64d%I64d",&l,&r,&t);
			for (int j=1;j<=t;j++)P[++len].l=l,P[len].r=r;
		}
		res=0;
		for (LL i=1;i<=len;i++)
		res+=(P[i].r-P[i].l-1)*(P[i].r-P[i].l)/2;
		for (int i=1;i<=len;i++){
			sort(P+i,P+len+1,cmp);
			for (int j=i+1;j<=len;j++)
			if (P[j].l<=P[i].r){
				if (P[i].r<P[j].r)swap(P[i].r,P[j].r);
			}
			else break;
		}
		ans=0;
		for (LL i=1;i<=len;i++)
		ans+=(P[i].r-P[i].l-1)*(P[i].r-P[i].l)/2;
		printf("Case #%I64d: %I64d\n",tt,ans-res);
	}
}
