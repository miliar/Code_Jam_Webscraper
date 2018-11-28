#include <iostream>
#include <cstdio>
#include <algorithm>
#define ll long long int

using namespace std;

int main()
{
    //freopen("D-large.in","r",stdin);
    //freopen("D-large.out","w",stdout);
    ll t;
    ll k, i, j, n;
    double arr[1010], brr[1010], crr[1010];
    scanf("%lld", &t);
    for (k = 1 ; k <= t; k++) {
        scanf("%lld", &n);
        for (i = 0 ; i < n ; i++) {
            scanf("%lf", &arr[i]);
        }
        for (i = 0 ; i < n ; i++) {
            scanf("%lf", &brr[i]);
            crr[i] = brr[i];
        }
        sort(arr,arr+n);
        sort(brr,brr+n);
        sort(crr,crr+n);
        ll z = 0;
        for (i = 0 ; i < n ; i++) {
            for (j = 0 ; j < n ; j++) {
                if (arr[i] < brr[j] && brr[j] != -1) {
                    z++;
                    brr[j] = -1;
                    break;
                }
            }
        }
        z = n-z;
        ll y = 0;
        for (i = 1 ; i < n  ;i++) {
           for (j = 0 ; j < n ; j++) {
               if (arr[j] > crr[i] && arr[j] != -1 && crr[i] != -1) {
                    y++;
                    crr[i] = -1;
                    arr[j] = -1;
                    break;
               }
           }
        }

        for (i = 0 ; i < n ; i++) {
            if(arr[i] != -1 && arr[i] > crr[0]) {
                y++;
                break;
            }
        }
        printf("Case #%lld: %lld %lld\n",k,y,z);
    }
    return 0;
}
