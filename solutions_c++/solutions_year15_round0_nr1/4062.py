#include <cstdio>
using namespace std;

int n;
char ch;
int p[2000];
int main(){
//freopen("out.txt", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int T=1; T<=test; T++){
        scanf("%d", &n); getchar();
        for (int i=0; i<=n; i++){
            ch = getchar();
            p[i] = ch-'0';
//            printf("%d\n", p[i]);
        }
        int ans = 0, sum = p[0];
        for (int i=1; i<=n; i++){
            if (sum < i){
                ans += i-sum;
                sum = i;
            }
            sum += p[i];
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
