#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
char s[105];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("o1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
		LL cnt=0;
		scanf("%s",s);
		int len=strlen(s);
		for (int i=1;i<len;i++){
			if (s[i-1]!=s[i])
			    cnt++;
		}
		if (s[len-1]=='-') cnt++;
		printf("Case #%d: %I64d\n",cas,cnt);
    }
    return 0;
}
