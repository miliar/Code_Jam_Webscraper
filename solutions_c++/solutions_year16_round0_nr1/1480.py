#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll solve(ll n) {
    vector<char> found(10, 0);
    int left = 10;

    for (ll i = 1; i != 10000; ++i) {
        ll curr = i * n;

        while (curr) {
            int dig = curr % 10;
            if (!found[dig]) {
                found[dig] = 1;
                --left;
            }
            curr /= 10;
        }

        if (!left) {
            return i * n;
        }
    }

    return -1;
}

int main() {
    freopen("C:\\Users\\timur\\Downloads\\A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);


    int t;
    scanf("%d", &t);

    for (int test = 0; test != t; ++test) {
        int n;
        scanf("%d", &n);

        printf("Case #%d: ", test + 1);
        
        ll ret = solve(n);
        if (ret == -1) {
            printf("INSOMNIA\n");
        } else {
            printf("%lld\n", ret);
        }
    }

    return 0;
}