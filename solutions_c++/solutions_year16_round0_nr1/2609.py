#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

bool ok(vector<int> &A) {
    int sum = 0;
    for(auto a: A)
        sum += a;

    return (sum == 10);
}

void update(vector<int> &A, int n) {
    while(n > 0) {
        int digit = n % 10;
        n = n / 10;
        A[digit] = 1;
    }
}

int main( void ) {

    freopen("input_a.txt", "r", stdin);
    freopen("output_a.txt", "w", stdout);

    int t;
    cin >> t;

    for(int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);

        int n;
        cin >> n;

        if(n == 0) cout << "INSOMNIA" << endl;
        else {
            int m = n;
            int k = 2;
            vector<int> mask(10, 0);
            update(mask, m);

            while(ok(mask) == false) {
                m = n * k;
                k += 1;
                update(mask, m);
            }

            cout << m << endl;
        }
    }
    return 0;
}
