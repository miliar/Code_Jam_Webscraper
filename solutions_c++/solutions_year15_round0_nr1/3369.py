#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>

#define f first
#define s second
#define pb push_back

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;
char str[1010][1010];
int main()
{
	int t,i,len,tot,ans,idx,n;
	
	scanf("%d",&t);
	idx = 1;
	while(t--)
	{
		scanf("%d %s",&n,str[idx]);
		len = strlen(str[idx]);
		tot = 0;
		ans = 0;
		for(i = 0;i < len;i++)
		{
			if((i > tot) && (str[idx][i] > '0'))
			{
				ans += (i - tot);
				tot += (str[idx][i] - '0') + (i - tot);	
			} 
			else
			{
				tot += (str[idx][i] - '0');
			}
	
		}
		printf("Case #%d: %d\n",idx++,ans);
	}
	return 0;
}
