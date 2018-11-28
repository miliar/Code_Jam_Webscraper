#include<cstdio>
#include<algorithm>
using namespace std;
char s[1010];
int main(){
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for(int icase = 1; icase <= T; icase++){
        scanf("%d%s", &n, s);
        n++;
        int sum = 0, ans = 0;//printf("%s\n", s);
        for(int i = 0; i < n; i++){
            if(sum >= i) sum+=(s[i]-'0');//printf("bbb = %d %d %d\n", i, sum, ans);
            else ans+=(i-sum), sum = (i+s[i]-'0');//printf("aaa = %d %d %d\n", i, sum, ans);
        }
        printf("Case #%d: %d\n", icase, ans);
    }
    return 0;
}
