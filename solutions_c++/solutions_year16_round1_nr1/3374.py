#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int testcase;
    cin>>testcase;
    for (int ii=1;ii<=testcase;++ii)
    {
        string x;
        cin>>x;
        string ans=string(1,x[0]);
        for (int i=1;i<x.length();++i)
            if (x[i]>=ans[0]) ans=x[i]+ans;
            else ans=ans+x[i];
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}
