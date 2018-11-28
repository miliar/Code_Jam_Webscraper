#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int T,ans=0;
	int X,R,C;
	cin>>T;
	while(T--)
	{
		ans++;
		scanf("%d%d%d",&X,&R,&C);
		if(X==1)
		{
			printf("Case #%d: GABRIEL\n",ans);
		}
		else if(((R*C)%2==0) && X==2 && (R>=2 || C>=2))
		{
			printf("Case #%d: GABRIEL\n",ans);
		}
		else if((X==3) && ((R*C)%3==0) && (R>=3||C>=3) && (R>1&&C>1))
		{
			printf("Case #%d: GABRIEL\n",ans);	
		}
		else if((X==4) && ((R*C)%4==0) && (R>=4||C>=4) && (R>2&&C>2))
		{
			printf("Case #%d: GABRIEL\n",ans);
		}
		else
		{
			printf("Case #%d: RICHARD\n",ans);
		}
	}
	return 0;
}