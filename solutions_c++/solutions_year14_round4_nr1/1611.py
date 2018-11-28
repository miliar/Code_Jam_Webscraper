#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
#include<iostream>
using namespace std;
typedef long long ll;
int s[10001];

int main()  
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	int n,x,ans;
	scanf("%d",&T);
	for(int rr=1;rr<=T;rr++)
	{
		scanf("%d%d",&n,&x);
		for(int i=0;i<n;i++)
			scanf("%d",s+i);
		sort(s,s+n);
		ans=0;
		int i=0,j=n-1;
		while(i<j)
		{
			if(s[i]+s[j]<=x)
				i++;
			j--;
			ans++;
		}
		if(i==j)
			ans++;
		printf("Case #%d: %d\n",rr,ans);
	}
	return 0;
}