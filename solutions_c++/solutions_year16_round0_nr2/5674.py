#include <bits/stdtr1c++.h>
#include <unistd.h>
using namespace std;

int ans = 0, len = 0;
string s = "";

int main() {
    int test; cin >> test;
    for (int t=1; t<=test; t++) {
        ans = 0;
        len = 0;
        s = "";
        cin >> s;
        len = s.size();
        bool flag = false;
        while (!flag) {
            int cnt = 0;
            for (int i=0; i<len; i++)
                cnt += (s[i]=='+');
            if (cnt == len)
                break;

            int pos1 = 0;
            while (s[pos1]=='+')
                pos1++;
            pos1--;
            if (pos1 == -1) {
                // find stretch of - and flip all of it till the bottom consecutive +
                int pos2 = len-1;
                while (s[pos2]=='+')
                    pos2--;
                pos2++;
                string tmp = s.substr(0,pos2);
                reverse(tmp.begin(), tmp.end());
                for (int i=0; i<pos2; i++)
                    if (tmp[i] == '+')
                        s[i] = '-';
                    else
                        s[i] = '+';
            }
            else {
                // found a stretch of +, flip that particular stretch
                string tmp = s.substr(0,pos1+1);
                reverse(tmp.begin(), tmp.end());
                for (int i=0; i<=pos1; i++) {
                    if (tmp[i] == '+')
                        s[i] = '-';
                    else
                        s[i] = '+';
                }
            }
            ans++;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
}
