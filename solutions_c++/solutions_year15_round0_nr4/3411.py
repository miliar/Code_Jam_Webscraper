#if 1

#include<stdio.h>
#include<conio.h>
#include<math.h>
#include <string.h>
#include<iostream>
using namespace std;

int main(){     
			unsigned int t;
			cin>>t;
			FILE *fp;
			fp=fopen("ominous_prob4.txt","w");
		 
			for(int i=0;i<t;i++)
				{
					 unsigned int X,R,C;
					 cin>>X>>R>>C;
					 int winner;
					 unsigned int RxC=R*C;
					 
					/* if(X>=RxC)
						 winner=0;
					 else 
						 winner=((RxC%X)==0);*/

		 switch(X){
					 case 1:
						// if(RxC==1)
							// winner=0;
						 //else
							 winner=1;
						 break;
					 
					 case 2:
						 if(RxC%2==0)
							 winner=1;
						 else
							 winner=0;
						 break;

					 case 3:
						 if(RxC%6==0||RxC%9==0)
							 winner=1;
						 else
							 winner=0;
						 break;

					case 4:
						 if(RxC%12==0||RxC%16==0)
							 winner=1;
						 else
							 winner=0;
						 break;
					 
					 }
					 //fprintf(fp,"s_max=%d no_of_ovation=%s Case #%d: %u\n",s_max,no_s,i+1,no_of_friends,stdout);
					 if(winner)
					 fprintf(fp,"Case #%d: GABRIEL\n",i+1,stdout);
					 else
					 fprintf(fp,"Case #%d: RICHARD\n",i+1,stdout);
			    }	   
		   getch();
           return 0;
}
#endif