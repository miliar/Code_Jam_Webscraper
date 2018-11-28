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
			fp=fopen("mushroom_monster.txt","w");
		 
			for(int i=0;i<t;i++)
				     {
					   unsigned int M[1010] ;
					   unsigned int N;//,mi;
					   unsigned int ans1;
					   unsigned int ans2;
					   unsigned int max_diff=0;
					   cin>>N;
					   //cin>>mi;
					   
					   ans1=0;
					   ans2=0;
					   

					   for(int ind1=0;ind1<N;ind1++)
					      {
					         cin>>M[ind1];
						      if(ind1>0)
						             {
							           if(M[ind1]<M[ind1-1])
							                 {
												  ans1+=M[ind1-1]-M[ind1];
												  if(M[ind1-1]-M[ind1]>max_diff)
												  max_diff=M[ind1-1]-M[ind1];
											 }
									 }
						  }

					   for(int ind1=0;ind1<N-1;ind1++)
								 {
									  if(M[ind1]>max_diff)
										 ans2+=max_diff;
									  else
										  ans2+=M[ind1];
					   
								 }
					   fprintf(fp,"Case #%d: %u %u\n",i+1,ans1,ans2,stdout);

					 }
					 
					 /*if(winner)
					 fprintf(fp,"Case #%d: GABRIEL\n",i+1,stdout);
					 else
					 fprintf(fp,"Case #%d: RICHARD\n",i+1,stdout);*/
			     
		   getch();
           return 0;
}
#endif