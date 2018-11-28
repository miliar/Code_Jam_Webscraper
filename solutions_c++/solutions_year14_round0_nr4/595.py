#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 1010

double a[MAXN];
double b[MAXN];
int    n, cnt;


int main() {
    int tc;
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i", &n);
        for(int i=0; i<n; ++i) scanf("%lf", &a[i]);
        for(int i=0; i<n; ++i) scanf("%lf", &b[i]);
        sort(a, a + n);
        sort(b, b + n);

        printf("Case #%i: ", tt);

        cnt = 0;
        for(int i=0, j=0; i<n; ++i) 
            if (a[i] > b[j]) cnt++, j++;
        printf("%i ", cnt);

        cnt = 0;
        for(int i=n-1, j=n-1, z=0; i >= 0; --i) 
            if (a[i] > b[j]) z++, cnt++;
            else j--;
        printf("%i\n", cnt);        
        
    
    }

}
