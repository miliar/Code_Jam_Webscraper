#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long T, N, cnt, temp;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> N;
        temp=N;
        vector<bool> V(10, false);
        cnt=10;
        if (!N) {
            cout << "INSOMNIA\n";
        } else {
            while (cnt) {
                int a=N;
                while (a) {
                    if (!V[a%10])
                        V[a%10]=true, cnt--;
                    a /= 10;
                }
                N += temp;
            }
            cout << N-temp << "\n";
        }
    }
    return 0;
}
