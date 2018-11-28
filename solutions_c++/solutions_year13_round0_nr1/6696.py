#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

bool compare(string a, string b) {
    bool res = true;
    for (size_t i = 0; i < a.length(); i++)
        res = res && (a[i] == 'T' || a[i] == b[i]);
    return res;
}

int main() {
    int T;
    string s1, s2, s3, s4;
    vector<string> strs;
    char buf[5];

    cin >> T;
    for (int t = 1; t <= T; t++) {

        cin >> s1 >> s2 >> s3 >> s4;
        cout << s1 <<"\n" << s2 <<"\n" << s3 << "\n" << s4 << "\n";
        cout << "Case #" << t <<": ";

        strs.clear();

        strs.push_back(s1);
        strs.push_back(s2);
        strs.push_back(s3);
        strs.push_back(s4);

        for (int i = 0; i < 4; i++) {
            sprintf(buf,"%c%c%c%c",s1[i],s2[i],s3[i],s4[i]);
            strs.push_back(buf);
        }

        sprintf(buf,"%c%c%c%c",s1[0],s2[1],s3[2],s4[3]);
        strs.push_back(buf);

        sprintf(buf,"%c%c%c%c",s1[3],s2[2],s3[1],s4[0]);
        strs.push_back(buf);

        bool X = false, O = false;
        for (size_t i = 0; i < strs.size(); i++) {
            X = X || compare(strs[i], "XXXX");
            O = O || compare(strs[i], "OOOO");
        }

        if (X) {
            cout << "X won" << endl;
            continue ;
        }

        if (O) {
            cout << "O won" << endl;
            continue ;
        }

        if ((""+s1+s2+s3+s4).find_first_of(".") != string::npos) {
            cout << "Game has not completed" << endl;
            continue ;
        }

        cout << "Draw" << endl;
    }

    return 0;
}
