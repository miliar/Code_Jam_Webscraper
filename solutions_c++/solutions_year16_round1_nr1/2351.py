#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {

    int test;
    cin >> test;

    for (int testnum = 0; testnum < test; testnum++) {
        string s, ujs="";
        cin >> s;
        ujs = s[0];
        int l = s.length();
        for (int i=1; i<l; i++) {
            if (s[i] < ujs[0])
                ujs += s[i];
            else
                ujs = s[i] + ujs;
        }

        cout << "Case #" << testnum+1 << ": " << ujs << endl;
    }

    return 0;
}
