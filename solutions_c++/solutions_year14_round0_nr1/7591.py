#include <stdio.h>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

#define LLI long long int
#define LLU long long unsigned int
#define LI  long int
#define LU  long unsigned
#define MAX(a,b) ((b)^(((a)^(b))&-((a)>(b))))
#define MIN(a,b) ((b)^(((a)^(b))&-((a)<(b))))
#define BUG printf("BUGGEeee");
#define PRINT(n) printf("%d",n);
#define MOD 1000000007
#define POWER2(v) (v && !(v & (v - 1)))
#define kk argv[1]



using namespace std;


int main(int argc,char* argv[])
{
	int T,K=0;
	scanf("%d",&T);
	while(T--)
	{K++;
		int begin,end,count=0,i,result;
		int a,b,A[16],C[16]={0},B[16],D[16]={0};
	scanf("%d",&a);
	for(i=0;i<16;i++)
	{scanf("%d",&A[i]);}
	scanf("%d",&b);
	for(i=0;i<16;i++)
	{scanf("%d",&B[i]);}
	end=(a)*4-1;
	begin=end-3;
	for(i=begin;i<=end;i++)
	{C[A[i]-1]++;}
	end=(b)*4-1;
	begin=end-3;
	for(i=begin;i<=end;i++)
	{D[B[i]-1]++;}
	for(i=0;i<16;i++)
	{if(C[i] && D[i])
		{count++;
			result=i+1;}}
	
	if(count==0)
	{printf("Case #%d: Volunteer cheated!\n",K);}
	else if(count==1)
	{printf("Case #%d: %d\n",K,result);}
	
	else
	{
		printf("Case #%d: Bad magician!\n",K);
		//printf("%d",count);
	}
	
}
	
	return 0;
	}


