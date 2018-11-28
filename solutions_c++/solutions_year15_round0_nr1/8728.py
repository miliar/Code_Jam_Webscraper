#include<iostream>
#include <stdio.h>
using namespace std;
int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    int t,smax,now,need;
    string s;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
        now=need=0;
        cin>>smax>>s;
        for(int i=0;i<=smax;i++)if(s[i]>'0')
        {
            if(i>now){need+=(i-now); now=i;}
            now+=(s[i]-'0');
        }
        cout<<"Case #"<<o<<": "<<need<<endl;
    }
    return 0;
}
