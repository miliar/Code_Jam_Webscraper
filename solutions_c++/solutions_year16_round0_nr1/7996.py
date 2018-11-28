#include <bits/stdc++.h>

using namespace std;

int main() {
    //ios_base::sync_with_stdio(false);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    vector<int> cnt(10, 0);
    for (int I = 0; I < T; I++) {
        long long n;
        cin >> n;
        long long ans = 0;
        cnt.assign(10, 0);

        printf("Case #%d: ", I + 1);

        if (!n) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        do {
            ans++;
            long long t = n * ans;
            while (t)
                cnt[t % 10ll]++, t /= 10ll;
        } while ((*min_element(cnt.begin(), cnt.end())) == 0);
        cout << n * ans << endl;
    }

    return 0;
}
