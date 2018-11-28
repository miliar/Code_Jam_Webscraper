#include <iostream>
#include<cstdio>
#include <bits/stdc++.h>
using namespace std;

main()
{
    freopen("A-large.in","r",stdin);
    freopen("outAL.txt","w",stdout);
    int t;
    cin>>t;
    string vec;
    int cas=1;
    while(t--)
    {

        int ma;
        cin>>ma>>vec;
        //cout<<vec;
        int s=0;
        int add=0;
        for(int i=0;i<=ma;i++)
        {
            if(s<i) {
               add+=(i-s);
               s+=(i-s);
            }
            s+=(vec[i]-48);
        }
        cout<<"Case #"<<cas++<<": "<<add<<endl;
    }

}
