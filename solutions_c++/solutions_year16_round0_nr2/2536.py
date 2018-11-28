#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int T;
char s[111], s1[111];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
    for(int cas = 1; cas <= T; cas++) {
    	scanf("%s",s1);
    	int n = 0, res = 0;
    	for(int i = 0; s1[i]; i++) {
            if(i && s1[i] == s1[i-1]) continue;
            s[n++] = s1[i];
    	}
    	for(int i = 0; i < n; i++) {
            if(s[i] == '-') res += 1+(i!=0);
    	}
    	printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
