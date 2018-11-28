#include<stdio.h>
#include<algorithm>
using namespace std;
#define N 1000

int main()
{
    int t, n, x, y, z;
    int i, j, f, naomi[N], ken[N], fire[N];
    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%d", &n);
        for(i = 0; i < n; i++) scanf(" 0.%d", &naomi[i]);
        for(i = 0; i < n; i++) scanf(" 0.%d", &ken[i]);
        sort(naomi, naomi+n);
        sort(ken, ken+n);

        for(i = 0; i < n; i++)
            fire[i] = 0;
        f = y = 0;
        for(i = n-1; i >= 0; i--) {
            for(j = 0; j < n; j++)
                if(fire[j] == 0 && naomi[j] > ken[i])
                    break;
            if(j == n) {
                for(j = 0; j < n && fire[j] == 1; j++);
                fire[j] = 1;
            }
            else {
                fire[j] = 1;
                y++;
            }
        }

        for(i = 0; i < n; i++)
            fire[i] = 0;
        f = z = 0;
        for(i = n-1; i >= 0; i--) {
            for(j = 0; j < n; j++)
                if(fire[j] == 0 && ken[j] > naomi[i])
                    break;
            if(j == n) {
                for(j = 0; j < n && fire[j] == 1; j++);
                fire[j] = 1;
                z++;
            }
            else {
                fire[j] = 1;
            }
        }
        printf("Case #%d: %d %d\n", x, y, z);
    }
    return 0;
}
