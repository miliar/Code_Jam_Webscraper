#include <iostream>
#include <string>

using namespace std;

int solved(string s)
{
    int res = 0;
    int plus = 0;
    int minus = 0;
    for (int i = 0; i < (int)s.length(); ++i) {
        if (s[i] == '-') {
            ++minus;
        } else if (s[i] == '+') {
            if (minus > 0) {
                if (plus > 0) {
                    res += 2;
                } else {
                    res += 1;
                }
            }

            plus = i + 1;
            minus = 0;
        }
    }

    if (minus > 0) {
        if (plus > 0) {
            res += 2;
        } else {
            res += 1;
        }
    }

    return res;
}

int main()
{
    int t;
    string s;
    cin>>t;

    for (int i = 1; i <= t; ++i) {
        cin>>s;
        cout<<"Case #"<<i<<": ";
        int res = solved(s);
        cout<<res<<endl;
    }
    return 0;
}
