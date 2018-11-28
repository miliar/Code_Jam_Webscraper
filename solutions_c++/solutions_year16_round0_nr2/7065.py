#include <iostream>
#include<string.h>
#include<stdlib.h>
#define ll long long
using namespace std;

int main()
{
    ll t;
    char a[100];
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        scanf("%s",a);
        ll count=0;
        for(ll j=0;j<strlen(a)-1;j++)
        {
            if(a[j+1]!=a[j])
                count++;
        }
        if(a[strlen(a)-1]=='+')
            cout<<"Case #"<<i<<": "<<count<<endl;
        else
            cout<<"Case #"<<i<<": "<<count+1<<endl;
    }
    return 0;
}

