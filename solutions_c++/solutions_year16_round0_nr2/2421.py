#include<bits/stdc++.h>
using namespace std;
const int maxn=1e4+100;
char ss[maxn];
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%s",ss);
		int n=strlen(ss),res=0;
		for(int i=0;i<n-1;++i)
			if(ss[i]!=ss[i+1])++res;
		if(ss[n-1]=='-')++res;
		printf("Case #%d: %d\n",cas,res);
	}
	return 0;
}
