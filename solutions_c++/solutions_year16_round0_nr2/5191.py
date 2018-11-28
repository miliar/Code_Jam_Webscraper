#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>


using namespace std;



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        string s;
        cin >> s;
        int cnt=0;
        char it=s[0];
        for (int j=1;j<s.size();j++)
        {
            if (s[j]!=it){cnt++;it=s[j];}
        }
        if (it=='-'){cnt++;}
        cout << "Case #" << i+1 << ": " << cnt << endl;
    }
}
