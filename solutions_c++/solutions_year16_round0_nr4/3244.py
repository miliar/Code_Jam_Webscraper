#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("Out.out", "w", stdout);
    int tt;
    int k, c, s;
    cin >> tt;
    for(int t = 0; t < tt; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> k >> c >> s;

        for(int i = 0; i < s; i++)
            cout << i + 1 << " ";
        cout << endl;
    }
    return 0;
}
