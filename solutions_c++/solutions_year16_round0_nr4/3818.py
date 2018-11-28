#include <iostream>
using namespace std;

void solve () {
    int k, c, s;
    cin >> k >> c >> s;
    for (int i=1; i<=s; i++)
        cout << i << " ";
    cout << endl;

}

void tile (string s, int c) {
    for (int i=1; i<c; i++) {
        string tmp = "";
        for (int j=0; j<s.size(); j++)
            if (s[j] == 'L')
                tmp += s;
            else tmp += string(s.size(), 'G');
        s = tmp;
    }
    
    cout << s << endl;
}

int main () {
    //string s = "LLLG";
    //tile (s, 2);
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        solve ();
    }
}