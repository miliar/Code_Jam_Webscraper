#include <iostream>
#include <fstream>
#include <stdio.h>
#define ll long long int
#define cin romeo
#define cout rumon
using namespace std;
int main()
{
    ifstream romeo("B-small-attempt0.in");
    ofstream rumon("B-small-attempt0.out");
    ll a, b, c, w, t, i, tc, j, k;
    cin>>t;
    for(tc=1;tc<=t;tc++)
    {
        w=0;
        cin>>a>>b>>k;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                c=i&j;
                if(c<k)
                    w++;
            }
        }
        cout<<"Case #"<<tc<<": "<<w<<endl;
    }
}
