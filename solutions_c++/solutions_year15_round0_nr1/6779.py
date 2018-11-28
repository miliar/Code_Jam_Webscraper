#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
        int s;
        cin >> s;
        string l;
        cin >> l;
        int cnt = 0;
        int standing = 0;
        for(int k=0;k<=s;k++) {
            if (l[k]=='0') continue;
            if (standing<k) {
                cnt += k-standing;
                standing = k;
            }
            standing += l[k]-'0';
        }
        cout << "Case #" << i+1 << ": " << cnt << endl;
    }
    return 0;
}