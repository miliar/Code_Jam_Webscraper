#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main() {

    int t;
    string s;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> s;
        int db = 0;
        while (s.length() > 0) {
            //#1
            while (s.length() > 0 && s[s.length()-1] == '+')
                s = s.substr(0, s.length()-1);
            if (s.length() == 0)
                break;
            // #2

            if (s[0] == '+') {
                db++;
                for (int i=0; i<s.length() && s[i]=='+'; i++)
                    s[i] = '-';
            }


            // #3
            string us="";
            for (int i=s.length()-1; i>=0; i--) {
                if (s[i] == '-')
                    us += "+";
                else
                    us += "-";
            }
            db++;
            s = us;
        }
        printf ("Case #%d: %d\n", test, db);
    }
}
