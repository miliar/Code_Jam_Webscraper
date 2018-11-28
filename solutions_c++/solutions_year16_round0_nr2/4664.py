#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;

void chsn(char *sn) {
    if (*sn == '+')
        *sn = '-';
    else
        *sn = '+';
}

int main()
{
    //freopen("test", "r", stdin);
    freopen("in2", "r", stdin);
    freopen("out2", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        string s;
        cin>>s;
        int t = 0;
        char sn = '-';
        for(int i = s.length()-1; i >= 0; --i){
            if (s[i] == sn) {
                t++;
                chsn(&sn);
            }
        }
        cout<<"Case #"<<testcase+1<<": "<<t<<endl;
    }
    return 0;
}
