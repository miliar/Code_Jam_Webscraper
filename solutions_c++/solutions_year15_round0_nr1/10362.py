#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("a,in","r",stdin);
	freopen("a.out","w",stdout);
    int t; cin >> t;
    for(int j = 1; j <= t; j++) {
        int n, ans = 0, sum = 0;
        cin >> n;
        for (int i = 0; i <= n; i++){
            char c;
            cin >> c;
            c -= '0';
            if (c && sum < i)
                ans += i - sum, sum = i;
            sum += c;
        }
        cout <<"Case #"<<j << ": "<<  ans << '\n';
    }
}