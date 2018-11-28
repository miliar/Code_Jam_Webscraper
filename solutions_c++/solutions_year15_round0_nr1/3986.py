#include<cstdio>
#include<cstring>
using namespace std;

int T, n, cas;
char buf[2000];
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    cas = 0; scanf("%d", &T);
    while(T--){
        scanf("%d %s", &n, buf);
        int cnt = buf[0] - '0', ans = 0;
        for (int i = 1; i <= n; i++){
            if (cnt < i){
                ans += i - cnt;
                cnt += i - cnt;
            }
            cnt += buf[i] - '0';
        }
        printf("Case #%d: %d\n", ++ cas, ans);
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
