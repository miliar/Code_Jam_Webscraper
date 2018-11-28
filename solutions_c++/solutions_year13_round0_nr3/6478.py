#include<iostream>
using namespace std;
int a[1005];
int main()
{
    a[1]=1;
    a[4]=1;
    a[9]=1;
    a[121]=1;
    a[484]=1;
    int t;
    cin>>t;
    for(int test=1; test<=t; test++)
    {
        int p, k;
        cin>>p>>k;
        int suma=0;
        for(int licz=p; licz<=k; licz++)suma+=a[licz];
        cout<<"Case #"<<test<<": "<<suma<<endl;
    }
}
