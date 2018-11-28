//counter culture
#include<iostream>
using namespace std;

int rev(int x)
{
    int r=0; //cout<<x<<" ";
    while(x)//for( ; x ; )
    {
        r*=10;
        r+=x%10;
        x/=10;
    }
    return r;
}
int main()
{
    int i,a[1000001]={0},T,n,r;
    a[1]=1;
    for(i=2;i<1000001;i++)
    {
        //cout<<"For "<<i<<"\n";
        if((i%10)==0) a[i]=a[i-1]+1;
        else if((r=rev(i))>=i)
        {
            a[i]=a[i-1]+1; //cout<<a[i]<<" 1 ";
        }
        else if(a[r]<a[i-1])
        {
            a[i]=a[r]+1; //cout<<a[i]<<" 2 ";
        }
        else a[i]=a[i-1]+1;
        //cout<<a[i]<<endl;
    }
    for(cin>>T,i=1;i<=T;i++)
    {
        cin>>n;
        cout<<"Case #"<<i<<": "<<a[n]<<endl;
    }
}
