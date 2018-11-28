#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int main()
{
    freopen("/home/garfield/下载/B-small-attempt0.in","r",stdin);
    freopen("/home/garfield/下载/ans0.txt","w",stdout);
    int a,b;
    int tt;
    cin>>tt;
    for (int pp=1; pp<=tt; pp++)
    {
        printf("Case #%d: ",pp);
        int i;
        cin>>a>>b;
        for (i=0; i<abs(a); i++)
        {
            if (a>0) cout<<"WE";
            else cout<<"EW";
        }
        for (i=0; i<abs(b); i++)
        {
            if (b>0) cout<<"SN";
            else cout<<"NS";
        }
        cout<<endl;
    }
}
