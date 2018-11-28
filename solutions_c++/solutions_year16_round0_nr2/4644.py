#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[110];


int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
       scanf("%s", s);
       int n = strlen(s);
       int ans = 0;
       if(s[0] == '-') ans ++;
       printf("Case #%d:", _++);
       for(int i = 1; i < n; i++) {
            if(s[i] != s[i-1]) ans++;
       }
       if(s[0] == '-' && s[n -1] == '+') ans--;
       if(s[0] == '+' && s[n -1] == '-') ans++;
       printf(" %d\n", ans);
	}

    return 0;
}
