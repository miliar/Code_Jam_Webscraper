#include<stdio.h>
long long P,Pow[101];
int N;
long long F(int n,long long p)
{
	if(p==0)return -1;
	int i;
	long long s=0;
	for(i=n-1;i>=0;i--){
		if(p<=Pow[i])return s;
		p-=Pow[i];
		s+=Pow[n-i];
	}
	return Pow[n]-1;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TC,T=0,i;
	scanf("%d",&TC);
	Pow[0]=1;
	for(i=1;i<=50;i++)Pow[i]=Pow[i-1]*2LL;
	while(TC--){
		printf("Case #%d: ",++T);
		scanf("%d%lld",&N,&P);
		printf("%lld %lld\n",F(N,P),Pow[N]-F(N,Pow[N]-P)-2);
	}
}