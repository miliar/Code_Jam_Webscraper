#include<bits/stdc++.h>
#include <iostream>
using namespace std;
#define ll long long
int main()
{
    //cout << "Hello World!" << endl;
    ll t;
    bool a[10];
    
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        for(int o=0;o<10;o++)
    {
        a[o]=false;
    }
        ll n,temp,k,i,mul=0;
        cin>>n;
        temp=n;
        if(n!=0)
        {
           for(i=1;i<=100;i++)
           {
               mul=n*i;
               for(k=mul;k>0;k=k/10)
               {
                   ll d= k%10;
                   a[d]=true;
               }
               for(k=0;k<=9;k++)
               {
                   if(a[k]==true)
                   continue;
                   else
                   break;
               }
               if(k==10)
               break;
           }
           
            cout<<"Case #"<<tc<<": "<<(i)*temp<<endl;
        }
        else
        {
            cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
        }
    //    cout<<"Case #"<<tc<<": "<<i*n<<endl;
        
    }
    return 0;
}

