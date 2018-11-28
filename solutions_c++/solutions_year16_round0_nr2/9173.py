#include <bits/stdc++.h>
using namespace std;

string flipString(string str, int r) {
    for(int k = 0; k<r; ++k) {
        if(str[k] == '+') {
            str[k] = '-';
        }
        else {
            str[k] = '+';
        }
    }
    return str;
}

int main() {
    
    freopen("input.txt", "r", stdin);//redirects standard input
    freopen("output.txt", "w", stdout);//redirects standard output
    
    long long int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        
        string str;
        cin >> str;
        int l = str.size();
        int pos = l, count = 0, ans = 0;
        for(int j = l-1; j>=0; --j) {
            if(str[j] == '-') {
                count++;
            }
            else {
                if(count) {
                    str = flipString(str, pos);
                    ans++;
                    j++;
                }
                pos = j;
                count = 0;
            }
        }
        
        if(count) {
            str = flipString(str, pos);
            ans++;
        }
        
        cout << "Case #" << i << ": " << ans << endl;
    }
    
	return 0;
}
