#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
    int t, n, c, i, j, ret, k, s;
    cin >> t;
    c = 1;
    while (c <= t) {
        cout<<"Case #"<<c<<":";
        cin >> k >> n >> s;
        for (i=1; i<=k; i++) {
            cout<<" "<<i;
        }
        cout<<endl;
        c++;
    }
}
