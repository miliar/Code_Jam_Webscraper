#if 1

#include<stdio.h>
#include<conio.h>
#include<math.h>
#include <string.h>
#include<iostream>

int main(){     
	int t;

	int ans;
	
	scanf("%d ",&t);
	FILE *fp;
	fp=fopen("gaas.txt","w");
		 
		   for(int l=0;l<t;l++)
		   {
			   int n,m;
			   scanf("%d ",&n);
					scanf("%d ",&m);
					int ans=0;//[10]={0,0,0,0,0,0,0,0,0,0};
                // char in[4][4];
					int in[100][100];
					int ck_row[100];
					int ck_col[100];
				// int dot=0;
				 for(int i=0;i<n;i++)
					 for(int j=0;j<m;j++)
						{
							scanf("%d",&in[i][j]);
							in[i][j]--;
							ck_row[i]=0;
							ck_col[j]=0;
					    }
					 for(int i=0;i<n;i++)
						 for(int j=0;j<m;j++)
						 {
						  if(in[i][j]>ck_row[i]) ck_row[i]= in[i][j];
						   if(in[i][j]>ck_col[j]) ck_col[j]=in[i][j];
						 }

						// for(int i=0;i<n;i++) printf("ck_row[%d]=%d\n",i,ck_row[i]);
						// for(int j=0;j<m;j++) printf("ck_col[%d]=%d\n",j,ck_col[j]);



						 for(int i=0;i<n;i++)
						 for(int j=0;j<m;j++)
						 {
						   if(ck_row[i]>in[i][j]&&ck_col[j]>in[i][j])
							   ans= 1;
						 }
						 fprintf(fp,"Case #%d:",l+1,stdout);     
						if(ans==1) fprintf(fp," NO\n",stdout);
						if(ans==0) fprintf(fp," YES\n",stdout);

		   }
		     
		   
		   getch();
           return 0;
}

#endif