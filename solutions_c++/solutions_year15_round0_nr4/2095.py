#include<bits/stdc++.h>
using namespace std;
bool possible(int x, int r, int c)
{
	if((r*c)%x)
		return true;
	if(r<c)
		swap(r,c);
	int noe=(r*c)/x;
	if(x==1 || x==2)
		return false;
	if(x==3)
	{
		if(c==1)
			return true;
		else
			return false;
	}
	if(x==4 || x==5)
	{
		if(c<=2)
			return true;
		else 
			return false;
	}
	if(x==6)
	{
		if(c<=4)
			return true;
		else
			return false;
	}
	if(x>=7)
		return true;
}
int main()
{
	int t,tt,x,r,c;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d %d %d",&x,&r,&c);
		if(possible(x,r,c))
			printf("Case #%d: RICHARD\n",tt);
		else
			printf("Case #%d: GABRIEL\n",tt);
	}
	return 0;
}