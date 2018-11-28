#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
    int T,j;
    cin>>T;
    for(j=1;j<=T;j++)
    {
        string s;
        string o="";
        cin>>s;
        int len,i;
        len=s.length();
        o=o+s[0];
        for(i=1;i<len;i++)
        {
            if(s[i]<o[0])
            {
                o=o+s[i];
            }
            else
            {
                o=s[i]+o;
            }
        }
        cout<<"Case #"<<j<<": "<<o<<"\n";
    }
    return 0;
}
