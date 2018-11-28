#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large (1).in","rt",stdin);
    freopen("A-smalllsl.out","wt",stdout);
    int n,i,smax,j,cnt=0,num,k,count=0,in;
    char input[25535];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
	cnt=0,count=0;
        scanf("%d",&smax);
	cin>>input;
	for(j=0;j<smax+1;j++)
	{
		cnt=0;
		for(k=0;k<j;k++)
		{
			in= input[k]-'0';
			cnt+=in;
		}
		if(cnt+count<j)
			count+=(j-cnt-count);
	}
	printf("Case #%d: %d \n",i+1,count);	
    }
   
   return 0;
} 	
