#include<stdio.h>
#include<algorithm>
using namespace std;
int d[1000];
int e[1000];
int f[1000];
int zahyou[2000];
long long v[2000];
int mod=1000002013;
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b,c;
		scanf("%d%d",&a,&b);
		for(int i=0;i<b;i++)scanf("%d%d%d",d+i,e+i,f+i);
		long long wolf=0;
		for(int i=0;i<b;i++){
			wolf=(wolf+(long long)f[i]*a%mod*(e[i]-d[i])%mod-(long long)f[i]*(e[i]-d[i]-1)%mod*(e[i]-d[i])%mod*500001007%mod+mod)%mod;
		}
		for(int i=0;i<b;i++){
			zahyou[i*2]=d[i];
			zahyou[i*2+1]=e[i]+1;
		}
		std::sort(zahyou,zahyou+b*2);
		for(int i=0;i<2000;i++)v[i]=0;
		long long ret=0;
		for(int i=0;i<b;i++){
			int L=upper_bound(zahyou,zahyou+b*2,d[i])-zahyou-1;
			int R=lower_bound(zahyou,zahyou+b*2,e[i]+1)-zahyou;
			for(int j=L;j<R;j++)v[j]+=f[i];
		}
		for(int i=0;i<2*b;i++){
			int at=-1;
			long long MIN=99999999999999LL;
			for(int j=0;j<2*b;j++){
				if(v[j]&&MIN>v[j]){
					MIN=v[j];
					at=j;
				}
			}
			if(!(~at))break;
			int L=at;
			int R=at;
			while(1){
				if(L&&v[L-1])L--;
				else break;
			}
			while(1){
				if(R<2*b-1&&v[R+1])R++;
				else break;
			}
			int dist=zahyou[R+1]-zahyou[L];
		//	printf("%lld %d %d\n",MIN,a,dist);
			ret=(ret+MIN*a%mod*(dist-1)%mod-MIN*(dist-1)%mod*(dist-2)%mod*500001007%mod+mod)%mod;
			for(int i=L;i<=R;i++)v[i]-=MIN;
		}
		printf("Case #%d: %lld\n",t,(wolf-ret+mod)%mod);
	}
}