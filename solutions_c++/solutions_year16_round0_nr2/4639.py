#define N (1<<10)
#include <bits/stdc++.h>
using namespace std;

char s[N];
int T,cas;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	for(cin>>T;T--;)
	{
		cin>>s;
		int cnt=1;
		for(int i=1;s[i];i++)
			if(s[i]!=s[i-1]) cnt++;
		if((s[0]=='+' && (cnt&1)) || ((s[0]=='-') && !(cnt&1))) cnt--;
		printf("Case #%d: %d\n",++cas,cnt);
	}
	return 0;
}
