#include<iostream>
using namespace std;
int main()
{
    long int i,j,k,l,t;
    long long n,m;
    long int a[41]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001};
    long long b[42];
    cin>>t;
    for(i=0;i<40;i++)
    {
        b[i]=(long long)a[i]*a[i];
    }
    for(i=1;i<=t;i++)
    {
        cin>>n;
        cin>>m;
        k=0;
        l=0;
        while(b[k]<n)
        {
            k++;
        }
        while(b[k]<=m)
        {
            k++;
            l++;
        }
        if(i==t)
        {
            cout<<"Case #"<<i<<": "<<l;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<l<<endl;
        }
    }
}
