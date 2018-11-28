#include<bits/stdc++.h>
typedef long long int lli;
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int tt;
    cin>>tt;
    for(int k=1; k<=tt; k++)
    {
        lli a[10];
        memset(a,0,sizeof(a));
        lli n;
        cin>>n;
        if(n == 0)
        {
            cout<<"Case #"<<k<<": ";
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            lli t,full=0,j=1,r;
            while(1)
            {
                t=n*j;
                r=t;
               //  cout<<t<<endl;
                j++;
                while(t)
                {
                    a[t%10]++;
                    t=t/10;
                    int i;
                    for(i=0; i<10; i++)
                    {
                        if(a[i] == 0)
                            break;
                    }
                    if(i == 10)
                    {
                       // cout<<"Full checked everything is non zero atleast ones"<<i<<endl;
                        full=1;
                        break;
                    }
                }
               //  cout<<"Full:="<<full<<endl;
                if(full == 1)
                    break;

            }
            cout<<"Case #"<<k<<": ";
            cout<<r<<endl;
        }


    }
    return 0;
}
