#include <iostream>
#include <string>

using namespace std;

string solve(string s) {
    string r = "";
    for (int i = 0; i < s.length(); i++) {
        if (r.length() == 0 || s[i] >= r[0])
            r = s[i] + r;
        else
            r += s[i];
    }
    return r;
}
int main() {
    int n;
    cin >> n;
    string s;
    for (int i = 0; i < n; i++)  {
        cin >> s;
        printf("Case #%d: %s\n",i+1,solve(s).c_str());
    }
}
