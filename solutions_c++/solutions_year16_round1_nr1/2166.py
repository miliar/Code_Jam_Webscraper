#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
char s[1010];

void dfs(int l,int r) {
    int mp = l;
    for(int i = l+1; i <= r; i++) if(s[i] >= s[mp]) {
		mp = i;
    }
    printf("%c",s[mp]);
    if(mp>l) dfs(l, mp-1);
    for(int i = mp+1; i <= r; i++) printf("%c",s[i]);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T, n;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++) {
		scanf("%s",s);
		n = strlen(s);
        printf("Case #%d: ",cas);
        dfs(0, n-1);
        puts("");
	}
    return 0;
}
