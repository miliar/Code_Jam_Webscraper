#include <iostream>
#include <algorithm>
using namespace std;

int arr[1010];

void go() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    long long t = 1LL << 62LL;
    for (int j = 1; j <= 1000; j++) {
        long long s = 0;
        for (int i = 0; i < n; i++) {
            s += (arr[i] + j - 1) / j - 1;
        }
        t = min(t, s + j);
    }
    cout << t;
}

int main() {
    int testn;
    cin >> testn;
    for (int i = 0; i < testn; i++) {
        cout << "Case #" << i + 1 << ": ";
        go();
        cout << endl;
    }
}