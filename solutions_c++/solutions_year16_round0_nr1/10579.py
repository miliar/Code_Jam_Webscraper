#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
 
using namespace std;

bool flag[12];
 
int main()
{
	int n,T,i,j,N;
	scanf("%d",&T);
	//freopen ("friday.out", "w", stdout) ;
	for(int t=1;t<=T;t++)
	{	
		memset(flag,false,sizeof(flag));
		scanf("%d",&N);
		if(N==0)
			printf("Case #%d: INSOMNIA\n",t);	
		else 
		for(i=1;i<=1000000;i++)
		{	
			n=N*i;
			int m=n;
			while(n!=0)
			{
				//printf("%d ",n%10);
				flag[n%10]=true;
				n/=10;
			}
			for(j=0;j<=9;j++)
					if(flag[j]==false)
						break;
			if(j==10)
			{
				printf("Case #%d: %d\n",t,m);
				break;
			}		
		}
	} 
	return 0;
}
