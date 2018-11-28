#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
    int t,ca=1;
    long int a,b,k,c;

    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        c = 0;
        cin>>a>>b>>k;
        for(long int i=0;i<a;i++)
            for(long int j=0;j<b;j++)
                if((i&j)<k)
                    c++;
        cout<<"Case #"<<ca++<<": "<<c<<endl;
    }
}

