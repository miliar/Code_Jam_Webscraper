#include<bits/stdc++.h>
using namespace std;
const int maxn=2e3;
char s[maxn];
bool check(int n)
{
	for(int i=0;i<n;++i)
	{
		//cout <<s[i]<<endl;
		if(s[i]=='-')return false;
	}
	return true;
}
void solve(int cas)
{
	int k,ans=0;
	scanf("%s %d",s,&k);
	int n=strlen(s);
	for(int i=0;i<n;++i)
	{
		if(s[i]=='-')
		{
			for(int j=i;i+k<=n&&j<i+k;++j)
				if(s[j]=='-')s[j]='+';
				else s[j]='-';
			++ans;
		}
	}
	//cout <<n<<" "<<ans<<" "<<s<<endl;
	if(!check(n))printf("Case #%d: IMPOSSIBLE\n",cas);
	else printf("Case #%d: %d\n",cas,ans);
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
		solve(cas);
	return 0;
}
