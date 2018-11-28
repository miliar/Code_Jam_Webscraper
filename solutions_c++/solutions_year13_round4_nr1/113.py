#include<stdio.h>
#include<algorithm>
using namespace std;
struct A{
	int a,b,c;
}w[1001];
struct B{
	int a,b;
	bool operator <(const B &p)const{
		return a<p.a;
	}
}o[1001];
long long S[3001],TP[3001],Res,Mod=1000002013,lN,TN,Sum,tt,d[3001];
long long F(long long a){
	return (a*lN-a*(a-1)/(long long)2)%Mod;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TC,T,N,M,i,j,c,C;
	scanf("%d",&TC);
	while(TC--){
		printf("Case #%d: ",++T);
		scanf("%d%d",&N,&M);
		lN=N;
		c=0;
		Sum=0;
		for(i=0;i<M;i++){
			scanf("%d%d%d",&w[i].a,&w[i].b,&w[i].c);
			o[c].a=w[i].a,o[c].b=c;c++;
			o[c].a=w[i].b,o[c].b=c;c++;
			Sum+=F(w[i].b-w[i].a)*(long long)w[i].c;
			Sum%=Mod;
		}
		sort(o,o+c);
		C=0;
		d[0]=o[0].a;
		for(i=0;i<c;i++){
			if(i && o[i].a!=o[i-1].a){
				C++;
				d[C]=o[i].a;
			}
			if(o[i].b&1) w[o[i].b>>1].b=C;
			else w[o[i].b>>1].a=C;
		}
		for(i=0;i<M;i++){
			for(j=w[i].a;j<w[i].b;j++)S[j]=S[j]+(long long)w[i].c;
		}
		Res=0;
		long long ad,bd;
		for(i=0;i<C;i++){
			ad=0,bd=d[i+1]-d[i];
			TP[i+1]=S[i];
			Res=(Res+F(bd)*TP[i+1])%Mod;
			S[i]=0;
			TN=lN;
			for(j=i+2;j<=C;j++){
				ad=bd;
				bd=d[j]-d[i];
				TN--;
				TP[j]=TP[j-1];
				if(TP[j]>S[j-1])TP[j]=S[j-1];
				S[j-1]-=TP[j];
				Res=(Res+(F(bd)-F(ad)+Mod)%Mod*TP[j])%Mod;
			}
		}
		printf("%lld\n",Sum-Res);
	}
}