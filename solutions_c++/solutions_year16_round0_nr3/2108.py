#include <string>
#include <map>
#include <sstream>
#include<vector>
#include<iostream>
using namespace std;

vector<int> a(14);
    vector<int> v(32);

    vector<long long> p(11);
void func(int n,vector<int> &v)
{ //cout<<n<<"alojha"<<endl;

    int i=0;

    for(i=0; i<14; i++)
    {
        a[13-i]=n%2;
        n=n/2;
    }

    for(i=0; i<14; i++)
    {
        v[i+1]=a[i];
        v[i+17]=a[i];
    }
    return ;
}

int main()
{
    int t,n,j;
    cin>>t>>n>>j;



    cout<<"Case #1:"<<endl;

    for(int i=2; i<11; i++)
    {
        long long pow=1;
        for(int j=0; j<16; j++)
        {
            pow=pow*i;
        }
        p[i]=pow+1;
    }

    for(int i=0; i<500; i++)
    {
        v[15]=1;
        v[0]=1;
        v[16]=1;
        v[31]=1;
        func(i,v);

        for(int  j=0; j<32; j++)
        {
            cout<<v[j];
        }
        cout<<" ";
        for(int j=2; j<11; j++)
        {
            cout<<p[j]<<" ";
        }
        cout<<endl;

    }

    return 0;
}
