#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int t,X,R,C,w;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
            scanf("%d %d %d",&X,&R,&C);
			   if(X==1)
				 {
				     w=1;
				 }
			   if(X==2)
			   {
				 if((R==1 && C==1) || (R==1 && C==3) || (R==3 && C==1) || (R==3 && C==3))
				{
				    w=2;
				 }
				 else{

                        w=1;
				 }
				}
				if(X==3)
				{
				if((R==1 || C==1) || (C==2 && R==2) || (R==2 && C==4)||(R==4 && C==2) || (R==4 && C==4))
				{
				    w=2;
				 }
				else
				{
				    w=1;
				 }
				}
				if(X==4)
				{
				if((R==3 && C==4)|| (R==4 && C==3) || (R==4 && C==4))
				{
				    w=1;
				 }
				else
				 {
				     w=2;
				}
		 }
		 if(w==1)
         {
             printf("Case #%d: GABRIEL\n",j);
         }
         else
         {
             printf("Case #%d: RICHARD\n",j);
         }
	}
}

