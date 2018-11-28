#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    string s;
    cin >> t;
    for(int testCase = 1; testCase <= t; ++testCase) {
        cin >> s;
        int count = 0;
        for(int i = s.size() - 1; i >= 0; --i) {
            if(s[i] == '-') {
                count += 1;
                for(int k = 0; k <= i; ++k) {
                    if(s[k] == '+') {
                        s[k] = '-';
                    } else {
                        s[k] = '+';
                    }
                }
            }
        }
        cout << "Case #"<<testCase<<": "<<count<<endl;
    }
    return 0;
}
