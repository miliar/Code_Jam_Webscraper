#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<queue>
#include<algorithm>
#define mod 10000007
#define INF 89999999999999LL
#define MAXN 1010
#define ll __int64
using namespace std;
char s[1100];

int main()
{
	//freopen("C:\\Users\\user\\Desktop\\in1.txt","r",stdin);
	//freopen("C:\\Users\\user\\Desktop\\out1.txt","w",stdout);
	int i,j,T,n,cas=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		n++;
		scanf("%s",&s);
		int cnt=0,ans=0;
		for(i=0;i<=n;i++)
		{
			if(s[i] > '1')
				cnt+=s[i]-'1';
			else if(s[i] == '1') continue;
			else if(s[i] == '0')
			{
				if(cnt == 0) ans++;
				else cnt--;
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}

