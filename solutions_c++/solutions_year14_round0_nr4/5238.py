#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t,i,j,n,x,ct1,ct2;
    double a[10],b[10];
    cin>>t;
    x=t;
    while(t--)
    {
        ct1=ct2=0;
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i];
        for(i=0;i<n;i++)
            cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        for(i=0,j=0;i<n;i++)
        {
            if(a[i]>=b[j])
            {
                ct1++;
                j++;
            }
        }
        for(i=0,j=0;i<n;i++)
        {
            if(b[i]>=a[j])
            {
                ct2++;
                j++;
            }
        }
        cout<<"Case #"<<x-t<<": "<<ct1<<" "<<n-ct2<<endl;
    }
    return 0;
}
