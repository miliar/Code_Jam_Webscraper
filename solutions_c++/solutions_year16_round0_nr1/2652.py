#include <iostream>
#include <set>
#include <map>
using namespace std;

const int N = 1000001;

int getResult(int n) {
    set<int> count;
    for (int i = 1; ; i++) {
        int val = n * i;
        while (val > 0) {
            count.insert(val % 10);
            val /= 10;
        }
        if (count.size() == 10) return i * n;
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("AA.out", "w", stdout);
    int n, ca;
    map<int, int> result;
    for (int i = 1; i < N; i++) {
        result[i] = getResult(i);
    }
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        cin >> n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i + 1);
        } else {
            printf("Case #%d: %d\n", i + 1, result[n]);
        }
    }
    return 0;
}
