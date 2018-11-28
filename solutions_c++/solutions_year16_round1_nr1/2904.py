#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>

using namespace std;

int T;
char S[1010];
string ans;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d\n",&T);
	for(int i=1,len;i<=T;++i) {
		ans = "";
		gets(S);
		len = strlen(S);
		ans = ans + S[0];
		for(int j=1;j<len;++j) {
			if(S[j]<ans[0])
				ans = ans + S[j];
			else
				ans = S[j] + ans;
		}
		printf("Case #%d: %s\n",i,ans.c_str());
	}
	return 0;
}

