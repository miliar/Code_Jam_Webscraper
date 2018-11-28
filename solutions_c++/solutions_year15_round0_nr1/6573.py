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
			fp=fopen("stand_prob1.txt","w");
		 
			for(int i=0;i<t;i++)
				{
					 unsigned int s_max;
					 char no_s[1010];
					 cin>>s_max;
					 gets(no_s);
					 unsigned int no_of_friends=0;
					 unsigned int test_var=16;
					 for(int j=0;j<=s_max;j++)
					    {
                          int at_s_j=no_s[j]-'0';
					      test_var=test_var+at_s_j;
						 // fprintf(fp,"%d %d %u\n",j,at_s_j,test_var,stdout);
						  if(test_var<j)
							{
							  no_of_friends++;
							  if (j!=s_max) no_s[j+1]++;
						    }
					    }

					 //fprintf(fp,"s_max=%d no_of_ovation=%s Case #%d: %u\n",s_max,no_s,i+1,no_of_friends,stdout);
					 fprintf(fp,"Case #%d: %u\n",i+1,no_of_friends,stdout);
			    }	   
		   getch();
           return 0;

}

#endif