#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <string>
#include <stack>
using namespace std;
stack<char> st;
void solve(string str) {
    //stack<char> st;
    int ans = 0;
    int len = str.length();
    while (1) {
        if (str[0] == '-') {
            for (int i = 0; i < str.length(); i++) {
                if (str[i] == '-') {
                    str[i] = '+';
                }
                else {
                    break;
                }
            }
            ans++;
        }
        else if (str[0] == '+') {
            int cnt = 0;
            int ant = 0;
            bool ff = true;
            for (int i = 0; i < str.length(); i++) {
                if (str[i] == '+' && ff) {
                    cnt++;
                }
                else if (str[i] == '-'){
                    ff = false;
                    ant++;
                }
                if (str[i] == '+' && !ff) {
                    break;
                }
            }
            if (cnt == str.length()) {
                cout<<ans << endl;
                return;
            }
            for (int i = 0;  i < ant + cnt; i++) {
                str[i] = '+';
            }
            ans += 2;
        }
    }
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int T;
    cin>>T;
    int t = 0;
    while (t < T) {
        t++;
        printf("Case #%d: ", t);
        string str;
        cin>>str;
        solve(str);
    }
    return 0;
}