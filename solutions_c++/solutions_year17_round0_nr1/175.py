#include<bits/stdc++.h>
using namespace std;
char rev(char c)
{
	return (c=='+')?'-':'+';
}
void execute()
{
	string S;
	int k;
	cin>>S>>k;
	int ans = 0;
	for(int i=0; i<S.size(); i++)
		if(S[i]=='-')
		{
			if(i+k-1>=S.size()) ans = -1;
			if(ans == -1) break;
			for(int j=0; j<k; j++) S[i+j] = rev(S[i+j]);
			ans++;
		}
	if(ans == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
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
