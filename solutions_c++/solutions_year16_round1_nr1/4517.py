#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll t, i, k;
    string j, s;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>s;
        vector<string> v;
        vector<string>::iterator it;
        if(s[0]=='A')
            v.push_back("A");
        if(s[0]=='B')
            v.push_back("B");
        if(s[0]=='C')
            v.push_back("C");
        if(s[0]=='D')
            v.push_back("D");
        if(s[0]=='E')
            v.push_back("E");
        if(s[0]=='F')
            v.push_back("F");
        if(s[0]=='G')
            v.push_back("G");
        if(s[0]=='H')
            v.push_back("H");
        if(s[0]=='I')
            v.push_back("I");
        if(s[0]=='J')
            v.push_back("J");
        if(s[0]=='K')
            v.push_back("K");
        if(s[0]=='L')
            v.push_back("L");
        if(s[0]=='M')
            v.push_back("M");
        if(s[0]=='N')
            v.push_back("N");
        if(s[0]=='O')
            v.push_back("O");
        if(s[0]=='P')
            v.push_back("P");
        if(s[0]=='Q')
            v.push_back("Q");
        if(s[0]=='R')
            v.push_back("R");
        if(s[0]=='S')
            v.push_back("S");
        if(s[0]=='T')
            v.push_back("T");
        if(s[0]=='U')
            v.push_back("U");
        if(s[0]=='V')
            v.push_back("V");
        if(s[0]=='W')
            v.push_back("W");
        if(s[0]=='X')
            v.push_back("X");
        if(s[0]=='Y')
            v.push_back("Y");
        if(s[0]=='Z')
            v.push_back("Z");
        for(i=1;i<s.length();i++)
        {
            vector<string> vt;
            for(it=v.begin();it!=v.end();it++)
            {
                j=*it;
                vt.push_back((j+s[i]));
                vt.push_back((s[i]+j));
            }
            v.clear();
            for(it=vt.begin();it!=vt.end();it++)
                v.push_back((*it));
        }
        sort(v.begin(),v.end());
        j=v.back();
        cout<<"Case #"<<k<<": "<<j<<endl;
    }
    return 0;
}
