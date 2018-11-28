#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t; cin>>t;
    for(int kase = 1;kase<=t;++kase)
    {
        int Smax; cin>>Smax;
        string s; cin>>s;
        int curCnt = 0;
        int res = 0;
        for(int i=0;i<s.size();++i)
        {
            int d = s[i]-'0';
            if(curCnt < i)
            {
                res+=(i-curCnt);
                curCnt+=(i-curCnt);
            }
            curCnt+=d;

        }
        cout<<"Case #"<<kase<<": "<<res<<"\n";


    }
}
