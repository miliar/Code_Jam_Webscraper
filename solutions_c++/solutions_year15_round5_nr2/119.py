#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<map>
#include<vector>
#include<set>
#include<assert.h>
using namespace std;
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RI64(x) scanf("%I64d",&(x))
#define RII64(x,y) scanf("%I64d%I64d",&(x),&(y))
#define RILL(x) scanf("%lld",&(x))
#define RIILL(x,y) scanf("%lld%lld",&(x),&(y))
#define FZ(i,n) for(int i=0;i<(n);i++)
#define PA(a,n) FZ(_1,n)printf("%d%c",(a)[_1],_1==(n)-1?10:32)
#define ePA(a,n) FZ(_2,n)fprintf(stderr,"%d%c",(a)[_2],_2==(n)-1?10:32)
#define SZ(x) ((int)x.size())
#define ALL(x) (x).begin(),(x).end()
#define pritnf printf
#define N 5140
using namespace std;
typedef long long int lnt;
typedef double dou;
int n,k;
lnt sum[N];
lnt d[N];
lnt r[N],l[N];
lnt ans,mx,mxi;
void go(){
	lnt tmp=0;
	lnt x=(sum[0]%k+k)%k;
	FZ(i,k){
		tmp+=l[mxi]-l[i];
		tmp=(tmp%k+k)%k;
	}
	lnt t2=0;
	FZ(i,k){
		t2+=mx-(r[i]-l[i]);
	}
	/*
	for(;t2&&tmp!=x;t2--){
		x++;
		x%=k;
	}
	*/
	for(;t2&&tmp!=x;t2--){
		tmp++;
		tmp%=k;
	}
	ans=min(ans,mx+(tmp!=x));
}
void gogo(){
	FZ(i,k)l[i]=0,r[i]=0;
	for(int i=1;i<n-k+1;i++){
		d[i]=sum[i]-sum[i-1];
	}
	for(int j=0;j<k;j++){
		lnt ss=0;
		for(int i=j;i+1<n-k+1;i+=k){
			ss+=d[i+1];
			l[j]=min(l[j],ss);
			r[j]=max(r[j],ss);
		}
	}
	mx=-(1ll<<62);
	mxi=-1;
	FZ(i,k){
		if(mx<r[i]-l[i]){
			mx=r[i]-l[i];
			mxi=i;
		}
	}
	assert(mxi!=-1);
	ans=1ll<<62;
	//go();
	FZ(j,k){
		sum[0]--;
		l[mxi]++;
		r[mxi]++;
		go();
	}
	//go();
}
void sol(int uuu){
	RII(n,k);
	FZ(i,n-k+1)RI64(sum[i]);
	gogo();
	/*
	FZ(i,(n-k+1)/2)swap(sum[i],sum[(n-k+1)/2-1-i]);
	gogo();
	*/
	pritnf("Case #%d: %I64d\n",uuu,ans);
}
int main(){
	//while(RI(n)!=EOF)sol(0);
	freopen("B-large.in","r",stdin);
	freopen("Bl.txt","w",stdout);
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++)sol(ti);
	}
	return 0;
}

