#include<bits/stdc++.h>
using namespace std;

char in[100];

int main()
{
	int test;
	scanf("%d",&test);getchar();
	for(int a=1;a<=test;a++)
	{
		scanf("%s",in);getchar();
		int len=strlen(in);
		int ans=0;
		int t=0;
		for(int b=len-1;b>=0;b--)
		{
			if(t==0)
			{
				if(in[b]=='-')
				{
					t=1;
					ans++;
				}
			}
			else if(t==1)
			{
				if(in[b]=='+')
				{
					t=0;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",a,ans);
	}
}
