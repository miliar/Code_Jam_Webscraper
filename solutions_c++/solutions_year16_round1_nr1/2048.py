#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string solved(string s)
{
    string res = "";
    for (int i = 0; i <(int)s.length(); ++i) {
        string tmp1 = res + s[i];
        string tmp2 = s[i] + res;
        if (tmp1.compare(tmp2) > 0) {
            res = tmp1;
        } else {
            res = tmp2;
        }
    }

    return res;
}

int main()
{
    int t;
    cin>>t;
    string s;
    for (int i = 1; i <= t; ++i) {
        cin>>s;
        cout<<"Case #"<<i<<": "<<solved(s)<<endl;
    }

    return 0;
}
