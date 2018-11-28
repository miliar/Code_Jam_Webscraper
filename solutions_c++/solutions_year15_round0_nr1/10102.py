#include <bits/stdc++.h>

using namespace std;

int arr[1001];

int main(int argc, char *argv[]) {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int i, n, tests, test, total, need, audience, my_var;
    scanf("%d", &tests);
    for(test=1; test<=tests; test++) {
        total = 0;
        need = 0;
        scanf("%d%d", &n, &audience);
        for(i = n; i >= 0; i--) {
            my_var = audience % 10;
            arr[i] = my_var;
            audience /= 10;
        }
        for(i = 0; i <= n; i++) {
            if(arr[i] > 0) {
                if(i <= total) {
                    total += arr[i];
                }
                else {
                    need += (i-total);
                    total += arr[i] + need;
                }
            }
        }
        cout<<"Case #"<<test<<": "<<need<<endl;
    }
    return 0;
}
