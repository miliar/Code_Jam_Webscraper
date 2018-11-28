//
// Created by 冯斯聪 on 16/4/15.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;

string WL(string s) {
    if (s.length()<=1)
        return s;

    string sub = s.substr(0, s.length()-1);
    string last = s.substr(s.length()-1, 1);
    string wl = WL(sub);
    bool flag = (last + wl) > (wl + last);
    return flag?(last + wl):(wl+last);
}



int main(void) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string s;
        cin >> s;
        string out = WL(s);
        cout << "Case #" << i+1 <<": ";
        cout << out << endl;
    }
    return 0;
}