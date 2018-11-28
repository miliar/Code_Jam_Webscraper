#include <cstdio>
#include <cstring>
using namespace std;
char s[105];
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
    freopen("sample2.out", "w", stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%s",s);
		int ans=0;
		int len=strlen(s);
		if(s[0]=='-')ans++;
		for(int j=1;j<len;j++)
		{
			if(s[j]!=s[j-1]){
				if(s[j]=='-')ans+=2;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}