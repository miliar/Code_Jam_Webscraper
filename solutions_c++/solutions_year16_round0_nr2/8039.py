#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	int i,j,k,t,n,m,count;
	char A[111];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%s",A);
		n=strlen(A);
		count=0;
		for(i=n-1;i>=0;i--)
		{
			if(A[i]=='-')
			{
				++count;
				for(j=0;j<=i;j++)
				{
					if(A[j]=='-')
						A[j]='+';
					else if(A[j]=='+')
						A[j]='-';
				}
			}
		}
		printf("Case #%d: %d\n",k,count);
	}
	return 0;
}
