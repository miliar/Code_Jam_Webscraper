#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int max (int a,int b){

	
	return a<b?a:b;
	
}
int asc (const void * a, const void * b)
{
  return ( *(float*)a - *(float*)b );
}
int desc (const void * a, const void * b)
{
  return ( *(float*)b - *(float*)a );
}

int main(){

	int t,caseno,i,j,n,win,lose,wino,win2;

	float tem;
		scanf("%d",&t);
	caseno=0;
	while(caseno++ < t){
vector<float> c1,c2;

	
		scanf("%d",&n);
		int flag[n],flag1[n];
		int ar[n][n];

		for(i=0;i<n;i++){
			flag[i]=1;
			flag1[i]=1;
		scanf("%f",&tem);
		c1.push_back(tem);
	}
		for(i=0;i<n;i++)
	{
		scanf("%f",&tem);
		c2.push_back(tem);
	}
		sort(c1.begin(),c1.end());
		sort(c2.begin(),c2.end());
/*
		for(i=0;i<n;i++){
			printf("%f  ",c1[i]);
		}
	
printf("\n");
		for(i=0;i<n;i++){
			printf("%f  ",c2[i]);
		}
		printf("\n");
		*/
		
		j=n-1;
		wino=0;
		win2=0;
	for(i=0;i<n;i++){

			for(j=0;j<n;j++){
ar[i][j]=0;
			}}
		for(i=0;i<n;i++){

			for(j=0;j<n;j++){
				ar[i][j]=0;
				if(flag[j]==1){
					if(c1[i] > c2[j])
					{	wino++;
						//printf("...got %f %f\n",c1[i],c2[j]);
						flag[j]=0;
						break;
					}
				}

			
			}
				
				
			}

		for(i=0;i<n;i++){

			for(j=0;j<n;j++){
						if(flag1[j]==1){
					if(c2[i] > c1[j])
					{	win2++;
						//printf("***got %f %f\n",c1[i],c2[j]);
						flag1[j]=0;
						break;
					}
				}
			}
				
				
			}

		printf("Case #%d: %d %d\n",caseno,wino,n-win2);
		
	}
return 0;
}