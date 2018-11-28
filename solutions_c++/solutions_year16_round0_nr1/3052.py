#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef long long li;

int cused;
int used[20];
int lf;

void add(li n) {
    do {
        li c = n % 10;
        n /= 10;

        if (used[c] < cused) {
            used[c] = cused;
            lf--;
        }
    } while (n > 0);
}

int main() {
    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        int n;
        cin >> n;
        //n = test;

        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }

        cused++;
        lf = 10;

        li i = 0;
        while (lf > 0) {
            i++;
            add(n * i);
        }

        cout << i * n << endl;
    }
    return 0;
}
