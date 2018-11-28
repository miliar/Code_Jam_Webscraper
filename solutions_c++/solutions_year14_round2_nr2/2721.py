#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    int t;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int a,b,k, c=0;
        cin>>a>>b>>k;
        for(int l=0; l<a; l++)
        {
            for(int m=0; m<b; m++)
            {
                if((l&m)<k) c++;
            }
        }
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
}
