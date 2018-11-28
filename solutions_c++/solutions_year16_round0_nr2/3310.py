#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x;
    cin>>t;
    ll T = t;
    string s;
    while(t--) {
        cin>>s;
        k = 0;
        while(true) {
            
            i=(s.length()-1);
            while(i>=0 && s[i]=='+') {
                i--;
            }
            if (i<0) {
                break;
            }
            j=0;
            if (s[0]=='+') {
                k++;
            }
            while(j<s.length() && s[j]=='+') {
                s[j] = '-';
                j++;
            }
            char c;

            for (j=0; j<=i; i--, j++) {
                c = s[j];
                s[j] = s[i];
                s[i] = c;
                if (s[i]=='+') {
                    s[i] = '-';
                }
                else {
                    s[i] = '+';
                }
                if (j!=i) {
                if (s[j]=='+') {
                    s[j] = '-';
                }
                else {
                    s[j] = '+';
                }
            }
            }
            k++;
        }
        cout<<"Case #"<<(T-t)<<": "<<k<<endl;
    }


    return 0;

}