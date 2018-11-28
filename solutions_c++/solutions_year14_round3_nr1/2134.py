#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    long long int i,p,q,j,k,t,result,l;
    char ch;
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>p>>ch>>q;
    j=100;

    for(i=0;i<=10;i++)
    {
        if(q==pow(2,i))
        {
            j=i;break;
        }
    }
    if(p>q || j==100)
    {
        cout<<"Case #"<<l<<": impossible"<<"\n";
        continue;
    }
    else if(p==q && q==1)
    {
        cout<<"0"<<"\n";
        break;
    }
    for(k=1;k<=j;k++)
    {
        if(p>=pow(2,j-k) && p<=pow(2,j-(k-1)))
        {
            result=k;break;
        }
    }
    cout<<"Case #"<<l<<": "<<result<<"\n";}
    return 0;
}
