#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int eps = 1e-7;
double a[1010], b[1010];
int main(){
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T, n, cnt = 1;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            scanf("%lf", &b[i]);
        }
        for(int i = 0; i < n; i++){
            scanf("%lf", &a[i]);
        }
        sort(a, a+n);
        sort(b, b+n);
        int pos = 0, res = 0;
        for(int i = 0; i < n; i++){
            while(pos < n && b[i] - a[pos]>eps){
                pos++;
            }
            if(pos < n && a[pos] - b[i] > eps) res++;
            pos++;
            if(pos >= n) break;
        }
        int max1 = n-1, max2 = n-1, min1 = 0, min2 = 0;
        int ret = 0;
        for(int i = 0; i < n; i++){
            if(b[max2] - a[max1] > eps){
                max2--;
                max1--;
                ret++;
            }
            else if(a[max1] - b[max2] > eps){
                min2++;
                max1--;
            }
            else {
                if(b[min2] - a[min1] > eps){
                    ret++;
                    min2++;
                    min1++;
                }
                else if(a[min1] - b[min2] > eps){
                    min2++;
                    max1--;
                }
                else{
                    min2++;
                    max1--;
                }
            }
        }
        printf("Case #%d: %d %d\n", cnt++, ret, n-res);
    }
    return 0;
}
