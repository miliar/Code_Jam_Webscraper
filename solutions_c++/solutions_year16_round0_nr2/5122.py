#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <cstring>

using namespace std;

int check[10000]={};
int cnt;
int n;
int flag=0;

int main()
{
	int x ;
	scanf("%d",&x);
	for (int i = 0; i < x; ++i)
	{
		char s[10000];
		scanf("%s",s);
		n =strlen(s);
		for (int i = 0; i < 10000; ++i)
		{
			check[i]=0;
		}
		for (int j = 0; j < n; ++j)
		{
			if (s[j]=='+')
			{
				check[j]=1;
			}
		}
		printf("Case #%d: ", i+1);
		int cnt=0;
		for (int j = 1; j < n; ++j)
		{
			if (s[j]!=s[j-1])
			{
				cnt++;
			}
		}
		cnt++;
		//printf("%d\n",cnt );
		if (cnt==1)
		{
			if (check[0]==1)
			{
				printf("0\n");
			}
			else
				printf("1\n");
		}
		else if (cnt%2==1&&cnt!=1)
		{
			if (check[0]==check[n-1]&&check[0])
			{
				printf("%d\n",cnt-1 );
			}
			else
				printf("%d\n",cnt );
		}
		else
		{
			if (check[0]==1&&check[n-1]==0)
			{
				printf("%d\n",cnt );
			}
			else
				printf("%d\n",cnt-1 );
		}
	}
	return 0;
}