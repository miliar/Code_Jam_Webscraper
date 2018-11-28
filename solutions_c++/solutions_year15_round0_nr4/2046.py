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
	int	flag = 0,n,i=0,j,index = 0,x,y,m,input,sum,ans;

	freopen ("d:/Codejam/D-small-attempt10.in","r",stdin);
	freopen ("d:/Codejam/D-small-attempt10.out","w",stdout);
	scanf("%d",&input);
	 string Ans;
	int X,R,C;
	while(input--)
	{
		scanf("%d%d%d",&X,&R,&C);
		Ans="GABRIEL";
		if(X == 1)
		{
			Ans="GABRIEL";
		}
		else if(X == 2)
		{
			if((R==1 && C==2) || (R==2 && C==1))
				Ans="GABRIEL";
			else if((R==1 && C==4) || (R==4 && C==1))
				Ans="GABRIEL";
			else if((R==2 && C==2) )
				Ans="GABRIEL";
			else if((R==2 && C==3) || (R==3 && C==2))
				Ans="GABRIEL";
			else if((R==2 && C==4) || (R==4 && C==2))
				Ans="GABRIEL";
			else if((R==3 && C==4) || (R==4 && C==3))
				Ans="GABRIEL";
			else if( (R==4 && C==4))
				Ans="GABRIEL";
			else
				Ans= "RICHARD";
		}
		else if(X == 3)
		{
			if((R==2 && C==3) || (R==3 && C==2))
				Ans="GABRIEL";
			else if((R==3 && C==4) || (R==4 && C==3))
				Ans="GABRIEL";
			else if((R==3 && C==3))
				Ans="GABRIEL";
			else
				Ans= "RICHARD";
		}
		else if(X == 4)
		{
			if( (R==4 && C==4))
				Ans="GABRIEL";
			else if((R==3 && C==4) || (R==4 && C==3))
				Ans="GABRIEL";
			else
				Ans= "RICHARD";
		}

		printf("Case #%d: ",++index);

		cout<<Ans<<"\n";
	}
	return 0;
}
