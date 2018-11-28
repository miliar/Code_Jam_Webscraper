#include<iostream>
using namespace std;
const int BUF = 1005;


string str;

void read() {
    cin >> str;
}


void work(int cases) {
    string ans = "";

    for (int i = 0; i < str.size(); ++i) {
        char ch = str[i];
        
        if (i == 0) {
            ans += ch;
        }
        else {
            int idx = 0;
            while (idx < ans.size() && ans[idx] == ch) ++idx;

            if (idx == ans.size() || ans[idx] > ch) {
                ans += ch;
            }
            else {
                ans = ch + ans;
            }
        }
    }
    
    cout << "Case #" << cases << ": " << ans << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
