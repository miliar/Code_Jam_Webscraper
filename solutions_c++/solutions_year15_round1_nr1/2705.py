typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
using namespace std;
int main()
{
    ll i,j,t,n,a[1000],w=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        ll sum1=0;
        ll maxi=0;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            if(i>0 && a[i]<a[i-1])
            {
                sum1+=a[i-1]-a[i];
                if((a[i-1]-a[i])>maxi)
                maxi=a[i-1]-a[i];
            }
            
        }
        ll sum2=0;
        for(j=0;j<n-1;j++)
        {
            if(a[j]<=maxi)
            sum2+=a[j];
            else
            sum2+=maxi;
        }
        cout<<"Case #"<<w++<<": "<<sum1<<" "<<sum2<<endl;
    }
    return 0;
}