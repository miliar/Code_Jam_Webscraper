#include<bits/stdc++.h>
#define ll long long int
#define inf 1000000000
#define mod 1073741824
using namespace std;

ll t,tt,n,i,j,k,l,flag,has[10];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<tt-t+1<<": "<<"INSOMNIA"<<endl;
            t--;
            continue;
        }
        for(i=0;i<10;i++)
            has[i]=0;
        j=1;
        while(1)
        {
            k=j*n;

            l=k;
            while(l)
            {
                has[l%10]=1;
                l/=10;
            }

            flag=1;
            for(i=0;i<10;i++)
            {
                if(has[i]==0)
                {
                    flag=0;
                    break;
                }
            }
            if(flag==1)
            {
                cout<<"Case #"<<tt-t+1<<": "<<k<<endl;
                break;
            }
            j++;
        }
        t--;
    }

    return 0;
}

