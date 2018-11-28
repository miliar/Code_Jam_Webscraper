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

//vector<long long > a,b;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        string s="",inp;
        cin >> inp;
        s+=inp[0];
        for (int j=1;j<inp.size();j++)
        {
            if (inp[j]>=s[0])
            {
                s=inp[j]+s;
            }
            else {s+=inp[j];}
        }
        cout << "Case #" << i+1 << ": " << s << endl;

    }
}
