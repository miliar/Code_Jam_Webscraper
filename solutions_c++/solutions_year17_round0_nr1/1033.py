#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;

const int N = 1005;
char s[N];
int n, k;

int check() {
    int ret = 0;
    For(i, n) {
        if(s[i] == '+') continue;
        if(i > n - k) return -1;
        ret++;
        for(int j = i; j < i + k; j++) 
            s[j] = s[j] == '+' ? '-' : '+';
    }
    return ret;
}

int main() {
    int T;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        scanf("%s%d", s, &k);
        n = strlen(s);
        int ans = check();
        printf("Case #%d: ", cas + 1);
        if(ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
	return 0;
}
