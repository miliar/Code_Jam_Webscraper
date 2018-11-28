#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	scanf("%d",&T);
	for(int t = 1; t<=T; t++)
	{
		int X,R,C;
		scanf("%d%d%d",&X,&R,&C);
		bool gabriel = true;
		if(X == 1)
		{
			gabriel = true;
		}
		else if(X == 2)
		{
			if((R==1 && C==2) || (R==2 && C==1))
				gabriel=true;
			else if((R==1 && C==4) || (R==4 && C==1))
				gabriel=true;
			else if((R==2 && C==2) )
				gabriel=true;
			else if((R==2 && C==3) || (R==3 && C==2))
				gabriel=true;
			else if((R==2 && C==4) || (R==4 && C==2))
				gabriel=true;
			else if((R==3 && C==4) || (R==4 && C==3))
				gabriel=true;
			else if( (R==4 && C==4))
				gabriel=true;
			else
				gabriel= false;
		}
		else if(X == 3)
		{
			if((R==2 && C==3) || (R==3 && C==2))
				gabriel=true;
			else if((R==3 && C==4) || (R==4 && C==3))
				gabriel=true;
			else if((R==3 && C==3))
				gabriel=true;
			else
				gabriel= false;
		}
		else if(X == 4)
		{
			if( (R==4 && C==4))
				gabriel=true;
			else if((R==3 && C==4) || (R==4 && C==3))
				gabriel=true;
			else
				gabriel= false;
		}

		if(gabriel)
			printf("Case #%d: GABRIEL\n",t);
		else 
			printf("Case #%d: RICHARD\n",t);
	}
	return 0;
}
