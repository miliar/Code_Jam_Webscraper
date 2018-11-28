#include<map>
#include<string>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<vector>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<climits>
#include<list>
#include<iomanip>
#include<stack>
#include<set>
using namespace std;
typedef long long ll;
char s[110];
int main()
{
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		scanf("%s",s);
		int len=strlen(s),ans=0;
		for(int i=1;i<len;i++)
			if(s[i]!=s[i-1])
				ans++;
		if(s[len-1]=='-')
			ans++;
		printf("Case #%d: %d\n",cs,ans);
	}
}
