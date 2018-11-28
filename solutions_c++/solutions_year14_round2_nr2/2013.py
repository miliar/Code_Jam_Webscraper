#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>


using namespace std;

#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define LL long long
#define forn(a,b) for(LL a=0; a<b; a++)
#define FOR1(a,b) for(LL a=1; a<=b;a++)
#define file freopen("B-small-attempt0.in","r",stdin)


int main()
{
    file;
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    forn(l,t)
    {
        int a,b,k;
        cin>>a>>b>>k;
        int ans=0;
        for(int i=0; i<a; i++)
            for(int j=0; j<b; j++)
                if((i & j) < k)
                    ans++;// cout<<i<<' '<< j<<endl;}
        /*int kil=0;
         for(int i=0; i<=a; i++)
            for(int j=0; j<=b; j++)
                if((i & j) < k && (i==j)) kil++;
        //ans -= kil/2;*/

        cout<<"Case #" << l+1<<": "<<ans<<endl;
    }
}
