#include<cstdio>
#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int cnt = 1;
	while(t--)
	{
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		if(x==1) printf("Case #%d: GABRIEL\n",cnt++);
		else if(x==2)
		{
			if((r*c)%2 ==0) printf("Case #%d: GABRIEL\n",cnt++);
			else printf("Case #%d: RICHARD\n",cnt++);
		}
		else if(x==3)
		{
			if((r*c)%3 ==0 && r>1 && c>1) printf("Case #%d: GABRIEL\n",cnt++);
			else printf("Case #%d: RICHARD\n",cnt++);
		}
		else if(x ==4)
		{
			if((r*c)%4 ==0 && r>2 && c>2) printf("Case #%d: GABRIEL\n",cnt++);
			 else printf("Case #%d: RICHARD\n",cnt++);
		}
	}
	return 0;
}
