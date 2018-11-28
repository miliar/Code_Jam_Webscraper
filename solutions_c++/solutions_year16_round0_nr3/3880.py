#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

bool testcoini(string s, int i, int n, long long int divis[10]) {
    long long int num = 0, ml = 1;
    for (int j = n-1; j >= 0; --j) {
        long long int nm = s[j] - '0';
        num = num + nm*ml;
        ml = ml*i;
    }
    long long int l = sqrt(ml);
    for (long long int j = 2; j <= l; ++j) {
        if (num%j == 0) {
            divis[i] = j;
            return true;
        }
    }
    return false;
}

bool testcoin(string s, int n) {
    long long int divis[11];
    for (int i = 2; i < 11; ++i) {
        if(!testcoini(s,i,n, divis))
            return false;
    }
    //cout<<divis[10];
    cout<<s;
    for (int i = 2; i < 11; ++i)
        cout<<" "<<divis[i];
    cout<<"\n";
    return true;
}

int main()
{
    //freopen("test", "r", stdin);
    freopen("in3", "r", stdin);
    freopen("out3", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        cout<<"Case #"<<testcase+1<<":\n";
        int n,j;
        cin>>n>>j;
        string s = "1";
        for(int i = 1; i < n-1; ++i)
            s+="0";
        s+="1";
        int fl = 0;
        while (j != 0 /*&& fl < 65000*/) {
            //fl++;
            if (testcoin(s,n))
                j--;
            //cout<<s<<" ";
            for (int i = n-2; n > 0; --i) {
                //cout<<s[i]<<" ";
                if (s[i] == '0') {
                    s[i] = '1';
                    break;
                }
                else
                    s[i] = '0';
            }
            //cout<<s<<"\n";
        }
        //cout<<"Case #"<<testcase+1<<": "<<t<<endl;
    }
    return 0;
}
