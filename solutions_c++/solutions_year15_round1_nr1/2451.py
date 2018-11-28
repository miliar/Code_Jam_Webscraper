#include<iostream>
#include<string.h>

using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int i;
        long int n,a[1005]={0},re1=0,re2=0;
        cin>>n;
        int rt=0;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]<=a[i-1])
                re1+=(a[i-1]-a[i]);
            if(a[i-1]-a[i]>rt)
                rt=(a[i-1]-a[i]);
        }
        for(i=0;i<n-1;i++)
        {
            if(a[i]>rt)
                re2+=rt;
            else
                re2+=a[i];
        }
        //re2-=a[n-1];
        cout<<"Case #"<<j<<": "<<re1<<" "<<re2<<endl;
    }
}
