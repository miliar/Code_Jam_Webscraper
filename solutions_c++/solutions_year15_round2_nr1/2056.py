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
int half1,half2;
void divide(int maximum){
	{
		if(maximum%2 == 0){
			half1= maximum/2;half2 = half1;
		}
		else{
			half1= maximum/2;half2 = half1+1;
		}
	}

}
int dp[1000005];
int main()
{
	int	flag = 0,n,i=0,j,index = 0,x,y,m,input,ans,position;

	freopen ("d:/Codejam/A-small-attempt3.in","r",stdin);
	freopen ("d:/Codejam/output.out","w",stdout);
	scanf("%d",&input);
	long long result=0,sum=0,minimum,reverse,rem;
		int A;
		memset(dp,0,sizeof(dp));
		
		//result=A;
		for(i=1;i<=19;i++)
			dp[i]=i;

		for(i=20;i<=1000000;i++)
		{
		reverse=0;
		n=i;
			while(n>0){
			reverse=reverse*10+n%10;
			n/=10;
			}
			if(i%10 == 0 || i <= reverse )
				reverse=i-1;

			dp[i] = std::min(dp[i-1]+1,dp[reverse]+1);
		}
	while(input--)
	{
		
		scanf("%d",&A);
		
		printf("Case #%d: ",++index);	
		cout<<dp[A]<<"\n";
	}
	return 0;
}
