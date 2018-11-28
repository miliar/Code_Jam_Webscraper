#include<iostream>
#include<string>
using namespace std;

int main() {
    int T,ans;
    string str;
    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        cin >> str;
        while(str[str.length()-1]=='+') {
            str.erase(str.length()-1);
        }
        if(str.length()==0) {
            cout << "Case #" << tc << ": 0" << endl;
            continue;
        }
        ans = 1;
        for(int c=1;c<str.length();c++) {
            if(str[c]!=str[c-1]) {
                ans++;
            }
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }
    return 0;
}
