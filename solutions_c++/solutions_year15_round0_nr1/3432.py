#include<bits/stdc++.h>
using namespace std;
int n;
string S;
void execute()
{
	cin>>n>>S;
	int cur = S[0]-'0',ans=0;
	for(int i=1; i<S.size(); i++)
	{
		int d = S[i]-'0';
		if(d && cur<i)
		{
			ans+=i-cur;
			cur = i;
		}
		cur+=d;
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("A.inp","r",stdin);
	freopen("A.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
