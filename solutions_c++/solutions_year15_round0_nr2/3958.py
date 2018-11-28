#include <cstdio>
#include <set>
using namespace std;
const int N = 1000;
multiset<int> ss;
multiset<int>::iterator it;
inline int get(){
    it = ss.end(); it--;
    return *it;
}
int main(){
//freopen("B.in", "r", stdin);
freopen("B.out", "w", stdout);
//freopen("out_B.txt", "w", stdout);
    int test;
    int n;
    int a[1005];
    scanf("%d", &test);
    for (int T=1; T<=test; T++){
        scanf("%d", &n);
        for (int i=1; i<=n; i++) scanf("%d", &a[i]);
        int ans = 1e9;
        for (int i=1; i<=N; i++){
            int cos = 0, opt = 0;
            for (int j=1; j<=n; j++){
                if (a[j] >= i) cos = i;
                else cos = max(cos, a[j]);
                int delta = a[j]/i; if (a[j]%i) delta ++;
                opt += delta-1;
            }
            ans = min(ans, cos+opt);
        }
        printf("Case #%d: %d\n", T, ans);
    }
//fclose(stdout);
    return 0;
}
