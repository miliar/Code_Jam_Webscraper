#include <cstdio> 
#include <cstring>
#include <algorithm> 
using namespace std;
int a[1010];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int n;
        scanf("%d", &n); 
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);    
        }  
        int sum1 = 0;
        int sum2 = 0;
        int Max = 0;
        for (int i = 1; i < n; i++) {
            if (a[i] < a[i - 1]) {
                     sum1 += a[i - 1] - a[i];
                     Max = max(Max, a[i - 1] - a[i]);
            }
        }
        for (int i = 1; i < n; i++) {
            sum2 += min(Max, a[i - 1]);    
        }
        
        printf("Case #%d: %d %d\n", t + 1, sum1, sum2);
    }    
}
