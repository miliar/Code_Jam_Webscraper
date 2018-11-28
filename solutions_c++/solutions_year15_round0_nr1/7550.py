#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
freopen("i.txt", "r", stdin);
freopen("o.txt", "w", stdout);
    int t, n;
    string s;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        cin >> n >> s;
        int sum = 0, ans = 0;
        for(int j = 0; j <= n; j++) {
            if(j > sum) ans +=  (j - sum), sum += (j - sum);
            sum += (int)(s[j] - '0');
        }

        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}

