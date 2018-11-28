#include<stdio.h>
#include<algorithm>
using namespace std;
long long w[38];
long double Res,Sum,tp1,tp2;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TC,T=0,i,N,j,k;
	long long B,M,TB,S,E,TT;
	scanf("%d",&TC);
	while(TC--)
	{
		printf("Case #%d: ",++T);
		scanf("%lld%d",&B,&N);
		for(i=0;i<N;i++){
			scanf("%lld",&w[i]);
		}
		for(i=N;i<=36;i++)w[i]=0;
		sort(w,w+37);
		Res=0;
		for(i=1;i<=36;i++)
		{
			S=w[i-1],E=B+w[36];
			while(S<=E)
			{
				TB=B;
				M=(S+E+1LL)/2LL;
				for(j=0;j<i;j++)
				{
					TB-=(M-w[j]);
				}
				for(j=i;j<=36;j++)
				{
					if(M>=w[j])TB-=(M+1LL-w[j]);
				}
				if(TB>=0){
					Sum=0;
					TT=0;
					for(j=0;j<i;j++)
					{
						TT+=M-w[j];
					}
					tp1=36.00L/(long double)i;
					Sum=(long double)TT*tp1;
					tp1=B;
					tp2=TB;
					tp1-=tp2;
					if(Res<Sum-tp1)Res=Sum-tp1;
					S=M+1;
				}
				else E=M-1;
			}
		}
		printf("%.10llf\n",Res);
	}
}