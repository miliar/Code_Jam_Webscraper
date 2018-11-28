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
#define N
using namespace std;
typedef long long int lnt;
typedef double dou;
dou eps=1e-10;
int sgn(dou k){return (k>-eps)-(k<eps);}
int n;
lnt V,X;
typedef struct{lnt R,C;}ele;
int cmp(ele a,ele b){
	return a.C>b.C;
}

vector<ele>a,b;
dou sol(int uuu){
	a.clear();
	b.clear();
	RI(n);
	dou tV,tX;
	scanf("%lf %lf",&tV,&tX);
	X=(lnt)round(10000*tX);
	V=(lnt)round(10000*tV);
	lnt sum=0,vv=0;
	int cz=0;
	FZ(i,n){
		ele t;
		dou tx,ty;
		scanf("%lf %lf",&tx,&ty);
		t.C=(lnt)round(10000*ty);
		t.R=(lnt)round(10000*tx);
		t.C-=X;
		assert(sum<=(1ll<<62)-t.C*t.R);
		sum+=t.C*t.R;
		vv+=t.R;
		if(t.C>0)a.push_back(t);
		else if(t.C<0){
			t.C=-t.C;
			b.push_back(t);
		}
		else{
			cz++;
		}
	}
	//dou      flag=(sgn(sum)>0)?1.0:-1.0;
	if(cz==0&&(SZ(a)==0||SZ(b)==0))return -7122;
	vector<ele>&e=(sum>0)?a:b;
	sum=abs(sum);
	dou Sum=sum,VV=vv;
	sort(ALL(e),cmp);
	FZ(i,SZ(e)){
		if(sgn(Sum)==0)break;
		dou dsum=min(Sum,(dou)(e[i].C*e[i].R));
		Sum-=dsum;
		VV-=dsum/e[i].C;
	}
	return (dou)V/VV;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("PB_l.txt","w",stdout);
	//while(RI(n)!=EOF)sol();
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++){
			dou res=sol(ti);
			printf("Case #%d: ",ti);
			if(sgn(res+7122)==0){
				puts("IMPOSSIBLE");
			}
			else{
				printf("%.10f\n",res);
			}
		}
	}
	return 0;
}

