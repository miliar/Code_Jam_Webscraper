#include <bits/stdc++.h>

using namespace std;

int ans[1000001];
bool digits[10];
int z;

void add(int x) {
    while (x > 0) {
        if (digits[x % 10] == false) {
            digits[x % 10] = true;
            ++z;
        }
        x /= 10;
    }
}


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    for (int i = 1; i < 1000001; ++i) {
        for (int j = 0; j < 10; ++j)
            digits[j] = false;
        z = 0;
        int j = i;
        add(j);
        while (z < 10) {
            j += i;
            add(j);
        }
        ans[i] = j;
    }
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        if (n == 0)
            cout << "INSOMNIA";
        else
            cout << ans[n];
        cout << '\n';
    }
    return 0;
}
