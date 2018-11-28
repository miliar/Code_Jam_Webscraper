#include<iostream>
using namespace std;

main() {
    int t;
    cin >> t;
    for (int c=1 ; c<=t ; c++) {
        string s;
        cin >> s;
        int pos = s.length()-1, ans=0;

        cout << "Case #" << c << ": ";

        while (pos >= 0) {
            if (ans%2==0) {
                if (s[pos] == '-')
                    ans++;
            }
            else
                if (s[pos] == '+')
                    ans++;
            pos--;
        }
        cout << ans << endl;
    }
}
