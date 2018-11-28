#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<deque>
#include<string> 
#include<iostream>
#include<vector>
#define LL long long
#define INF 0X7FFFFFFF
using namespace std;
int T;
char s[500];
inline void open()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
}
int main()
{
	open();
	scanf("%d",&T);
	int cas=0;
	while(T--)
	{
		string tmp;
		scanf("%s",s);
		int len=strlen(s);
		int ans=0;
		for(int i=len-1;i>=0;i--)
		{
			tmp="";
			if(s[i]=='-')
			{
 				for(int j=0;j<=i;j++)
					tmp+=s[j];
				//cout<<tmp<<endl;
				for(int j=0;j<=i;j++)
				{
					if(tmp[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				//printf("%s\n",s);
				ans++;
			}
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
