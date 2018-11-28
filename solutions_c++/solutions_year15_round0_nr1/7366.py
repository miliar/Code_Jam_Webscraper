#include <bits/stdc++.h>

using namespace std;

int arr[100009];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long int t, n;
    int cas = 1, frd;
    scanf("%lld", &t);
        while(t--) {
            scanf("%lld", &n);
            scanf("%1d", &arr[0]);
            int c = arr[0];
            frd = 0;
            for(int i = 1; i <= n; i++) {
                scanf("%1d", &arr[i]);
                if((c < i) && (arr[i] != 0)) {
                    frd += i - c;
                    c += i - c + arr[i];
                }
                else
                    c += arr[i];
            }
            printf("Case #%ld: %ld\n", cas++, frd);
        }
    return 0;
}
