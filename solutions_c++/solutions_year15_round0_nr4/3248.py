#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("d.txt","r",stdin);
	freopen("do.txt","w",stdout);	
	int t,in;
	scanf("%d",&t);
	for(in =1;in<=t;in++)
	{
		int x,r,c,y=0;
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",in);
		if(((r*c)%x) !=0)y=1;
		else if(x==3)
		{
			if(r==1||c==1)y=1;
		}
		else if(x==4)
		{
		if(r==1||c==1)y=1;
		else if(r==2||c==2)y=1;
		}
		if(y)printf("RICHARD\n");
		else printf("GABRIEL\n");


	}

}
