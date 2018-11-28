#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fcin("in.in");
    ofstream fcout("out.out");
    int tests;
    fcin>>tests;
    for (int t=1;t<=tests;t++)
    {
        int maxS;
        fcin>>maxS;
        string s;
        fcin>>s;
        int stood=0,res=0;
        for (int i=0;i<s.size();i++)
        {
            if (i>stood)
            {
                res+=i-stood;
                stood+=i-stood;
            }
            stood+=(int)(s[i]-'0');
        }
        fcout<<"Case #"<<t<<": "<<res<<endl;
    }
    return 0;
}
