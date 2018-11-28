#include<bits/stdc++.h>
using namespace std;
#define MIN(A,B) (A<B?A:B)
int solve(int p,int q)
{
	int t=q-1;
	while(t>0)
	{
		if(!(t&1))
			return -1;
		t=t>>1;
	}
	int x=0,y=0;
	while(p>0)
	{
		x++;
		p=p>>1;
	}
	while(q>0)
	{
		y++;
		q=q>>1;
	}
	return y-x;
}
int main()
{
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int p,q;
		char x;
		scanf("%d%c%d",&p,&x,&q);
		//printf("%d %d\n",p,q);
		int ans=solve(p,q);
		printf("Case #%d: ",t);
		if(ans==-1)
			printf("impossible\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
