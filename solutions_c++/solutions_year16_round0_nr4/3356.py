#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int t,x=0;

    cin>>t;
    while(t--)
    {
        x++;
        int k,c,s;
        cin>>k;
        cin>>c;
        cin>>s;
        long long n,i;
        long long z;


        if(c==1&&s<k)
        {
            cout<<"Case #"<<x<<": IMPOSSIBLE\n";
            continue;
        }

        z = k/2;
        if(k%2==1)
            z++;
        if(z>s)
        {
            cout<<"Case #"<<x<<": IMPOSSIBLE\n";
            continue;
        }

        n = k;
        if(c>2)
        {
            for(i=2;i<c;i++)
                n=n*k;

        }
        if(c==1)
        {
            cout<<"Case #"<<x<<":";
            for(i=1;i<=k;i++)
                cout<<" "<<i;
            cout<<"\n";
            continue;
        }
        cout<<"Case #"<<x<<":";
        int j = 1;
        long long a1=0, a2 = n,a3;
        j=k/2;
      //  cout<<j<<" l\n";
        for(i=1;i<=k/2;i++)
        {
            cout<<" "<<a1+2;
            a3 = a1+2;
            a1 = 2*i*a2 + 2*i;

        }

        //a3 = a3+n;
        i--;
        if(k%2==1)
            cout<<" "<<a1 +1 - 2*i;
        cout<<"\n";
       // cout<<n<<"\n";


    }
}
