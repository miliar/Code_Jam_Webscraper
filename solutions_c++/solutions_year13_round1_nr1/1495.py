#include<iostream>

void solve(int T)
{
	long long R,P,cnt=0;

	scanf("%I64d%I64d",&R,&P);
	while(true)
	{
		
		P-=2*R+1;
		if(P>=0) cnt++;
		else break;
		R+=2;
	}
	printf("Case #%d: %I64d\n",T,cnt);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,i;
	scanf("%d",&T);
	for(i=1;i<=T;i++) solve(i);
	return 0;
}