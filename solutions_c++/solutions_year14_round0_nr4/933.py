#include <stdio.h>
#include <algorithm>

bool   crescente(float x, float y) { return x < y; }
bool decrescente(float x, float y) { return x > y; }

float naomi[1001];
float ken  [1001];

using std::sort;

int main() {
    int t,n, i,j,k, x,y,z;

    scanf("%d", &t);
    for(x=1; x<=t; ++x) {
        scanf("%d",&n);
        for(i=0; i<n; ++i) scanf("%f", &naomi[i]);
        for(i=0; i<n; ++i) scanf("%f", &ken  [i]);

        sort(naomi, naomi+n, crescente);
        sort(ken  , ken  +n, crescente);

        int win;
        for(y=0,z=0, i=0,j=0,k=0; i<n; ++i) {
            win = naomi[i] > ken[j];
            y+= win;
            j+= win;

            while(k!=n && naomi[i] > ken[k]) {
                ++k;
            }
            win = k==n;
            z+=  win;
            k+= !win;
        }

        printf("Case #%d: %d %d\n", x,y,z);
    }
    return 0;
}
