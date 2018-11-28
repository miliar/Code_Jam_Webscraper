#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

using namespace std;

int main() 
{
	
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
    
    int tt;
    cin >> tt;
    
    for (int c = 1; c <= tt; ++c) {
        cout << "Case #" << c << ": ";
        string s;
        cin >> s;
        int ans = 0;
        for (int i = sz(s) - 1; i >= 0; --i) {
            if (s[i] == '-') {
                if (s[0] == '+') {
                    int k = 0;
                    for (; s[k] == '+'; ++k) ;
                    --k;
                    ++ans;
                    for (int j = 0; j <= k; ++j) {
                        s[j] = '-';
                    }
                }
                string t = "";
                for (int j = 0; j <= i; ++j) {
                    t += s[j];
                }
                reverse(all(t));
                for (int j = 0; j <= i; ++j) {
                    if (t[j] == '-') {
                        t[j] = '+';
                    } else {
                        t[j] = '-';
                    }
                }
                for (int j = 0; j <= i; ++j) {
                    s[j] = t[j];
                }
                ++ans;
            }
            //cout << s << "\n";
        }
        cout << ans << "\n";
    }
    
}
