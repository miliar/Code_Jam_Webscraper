#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int y[10000];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int test=1;test<=testcase;test++)
    {
        string x;
        int k,ans=0;
        cin>>x>>k;
        for (int i=0;i<x.size();i++)
            if (x[i]=='+') y[i]=1;
            else y[i]=0;
        for (int i=0;i<=x.size()-k;i++)
            if (!y[i])
            {
                ans++;
                for (int j=i;j<i+k;j++)
                    y[j]=1-y[j];
            }
        bool flag=false;
        for (int i=0;i<x.size();i++)
            if (!y[i])
            {
                cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
                flag=true;
                break;
            }
        if (!flag) cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
