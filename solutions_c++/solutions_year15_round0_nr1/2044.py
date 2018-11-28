#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n;
        string s;
        cin >> n >> s;
        int ans = 0;
        int ad = 0;
        for (int j = 0; j <= n; j++){
            if (s[j] > '0' && ans < j){
                ad += j - ans;
                ans = j;
            }
            ans += s[j] - '0';
        }
        cout << "Case #" << i + 1 << ": " << ad << endl;
    }
    return 0;
}
