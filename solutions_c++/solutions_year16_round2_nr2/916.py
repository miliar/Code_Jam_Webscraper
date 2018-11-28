#include <iostream>
#include <set>
#include <cmath>
#include <vector>
using namespace std;

bool fit(string& s1, string & s2) {
    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] != '?' && s1[i] != s2[i])
            return false;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; t++) {
        string s1, s2;
        cin >> s1 >> s2;
        int n=s1.size();
        int dif = 100500, cod = 100500, jam = 100500;
        string res1, res2;

        for (int a=0; a < pow(10, n); a++) {
            string num1 = to_string(a);
            while (num1.size() < n) {
                num1 = "0" + num1;
            }
            if (!fit(s1, num1)) continue;


            for (int b=0; b<pow(10, n); b++) {
                string num2 = to_string(b);
                while (num2.size() < n) {
                    num2 = "0" + num2;
                }
                if (!fit(s2, num2)) continue;

                int cur_dif = abs(a-b);
                if (cur_dif < dif || (cur_dif == dif && a < cod) || (cur_dif == dif && a == cod && b < jam)) {
                    dif=cur_dif;
                    cod=a;
                    jam=b;
                    res1=num1;
                    res2=num2;
                }
            }
        }

        printf("Case #%d: %s %s\n", t, res1.c_str(), res2.c_str());
    }
    return 0;
}
