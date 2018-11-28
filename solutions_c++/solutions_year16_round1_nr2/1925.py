#include<bits/stdc++.h>
using namespace std;
long long h[2503];
int main()
{
     ifstream cin("concom.in");
    ofstream cout("concom.out");
    long long i,t,cont=0,n,x,lelz;

    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<++cont<<": ";
        lelz=0;
        for(i=0;i<2503;++i) h[i]=0;
        cin>>n;
        for(i=0;i<n*n*2-n;++i)
        {

            cin>>x;
            h[x]++;
            //if(x==1) cout<<h[x]<<endl;
        }

        for(i=0;i<2503;++i)
        {
            if(h[i]%2==1)
            {
                cout<<i;
                lelz++;
                if(lelz!=n) cout<<' ';
            }
        }

        cout<<endl;
    }
}
