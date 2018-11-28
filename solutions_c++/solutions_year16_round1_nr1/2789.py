#include <string>
#include <iostream>
using namespace std;

string fun(string& s) {
    string ret = "";
    for(char c : s) {
        if(ret == "")
            ret += c;
        else {
            if(c >= ret[0])
                ret = c + ret;
            else
                ret += c;
        }
    }
    return ret;
}

int main() {
    int T, cas = 1;
    cin >> T;
    while(T--) {
        string s;
        cin >> s;
        cout << "Case #" << cas++ << ": ";
        cout << fun(s) << endl;
    }
    return 0;
}
