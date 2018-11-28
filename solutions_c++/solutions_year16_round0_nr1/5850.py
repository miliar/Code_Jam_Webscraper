#include <iostream>
#include <stdio.h>
#include <sstream>
#include <cstring>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    string s;
    long long input;
    long long test;
    bool flag[10];
    bool done;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        memset(flag,0,sizeof flag);
        cin >> input;

        if (input == 0)
            cout << "Case #" << tc << ": INSOMNIA" << endl;
        else {
            for (int i = 1; i <= 10000; i++) {
                test = input*i;

                stringstream ss;
                ss << test;
                s = ss.str();

                for (int j = 0; j < s.length(); j++) {
                    flag[ s[j]-'0' ] = true;
                }
                done = true;
                for (int j = 0; j < 10; j++) {
                    if (flag[j] == false)
                        done = false;
                }
                if (done) {
                    cout << "Case #" << tc << ": " << test << endl;
                    break;
                }
            }
        }
    }
}
