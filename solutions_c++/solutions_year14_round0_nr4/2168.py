#include <algorithm>
#include <cstdio>
using namespace std;
const int N = 1100;
int T,n;
double a[N],b[N];
int main() {
    scanf("%d",&T);
    for (int C = 1;C <= T;C++) {
        scanf("%d",&n);
        for (int i = 0;i < n;i++) scanf("%lf",a+i);
        for (int i = 0;i < n;i++) scanf("%lf",b+i);
        int x = 0,y = 0;
        b[n] = 1;
        for (int i = 0;i < n;i++) {
            int k = n;
            for (int j = 0;j < n-i;j++)
                if ((b[j] > a[i])&&(b[j] < b[k]))
                    k = j;
            if (k == n) {
                y++;
                for (int j = 0;j < n-i;j++)
                    if (b[j] < b[k]) k = j;
            }
            swap(b[k],b[n-i-1]);
        }
        sort(a,a+n);
        sort(b,b+n);
        int p = 0,q = n-1;
        for (int i = 0;i < n;i++) {
            if (a[i] > b[p]) {
                x++;p++;
            } else q--;
        }
        printf("Case #%d: %d %d\n",C,x,y);
    }
    return 0;
}
