#include <iostream>
#include <string.h>
#include <set>
#include <cstring>
#include <cmath>
#include <fstream>
using namespace std;
typedef long long int ll;
set<ll> sett1;


int main()
{

    freopen("input.in", "r", stdin);
   freopen("output.txt", "w", stdout);
    long long int test;
    cin>>test;
    ll i;
    ll c=test;
    for( i=0;i<test;i++)
    {
        string aa,bb;
        cin>>aa;
        ll k=0;
        ll m=0;
        for( m=0;m<aa.length();m++)
        {
            if(m==0)
                bb=bb+aa[m];
            else
            {
                if(aa[m]>=bb[0])
                    bb=aa[m]+bb;
                else
                    bb=bb+aa[m];
            }
        }
        cout<<"Case #"<<i+1<<": "<<bb;
        if(c-i+1)
        cout<<endl;
    }
    return 0;
}
