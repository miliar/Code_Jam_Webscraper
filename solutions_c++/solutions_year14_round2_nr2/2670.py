#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long n;
    long long a;
    long long b;
    long long k;
    long long c = 0;

    cin >> n;
    for (int x = 0; x < n; x++) {
        c = 0;
        cin >> a >> b >> k;
        if (b > a) {
            swap(a,b);
        }
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k) {
                   c++;
                }
            }
        }
        cout << "Case #" << x+1 << ": " << c << endl;
    }

    return 0;
}
