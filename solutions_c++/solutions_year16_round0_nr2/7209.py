#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int t=1;t<=n;t++)
    {
        string x;
        cin>>x;
        ll cnt=0;
        bool f=0;
        if(x[0]=='-')
            cnt++;
        else
            f=1;
        for(int i=1;i<x.size();i++)
        {
            if(x[i]=='+')
                f=1;
            else
            {
                if(f==1)
                {
                    cnt+=2;
                }
                f=0;
            }
        }
        cout<<"Case #"<<t<<": "<<cnt<<endl;
    }
}
