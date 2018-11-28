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
#include <queue>
#include <memory.h>

using namespace std;

#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define LL long long
#define forn(a,b) for(LL a=0; a<b; a++)
#define FOR1(a,b) for(LL a=1; a<=b;a++)
#define fori(a,z,b) for(LL a=z; a<=b;a++)
#define sortV(a) sort(A.begin(), A.end())
#define file freopen("input.txt","r",stdin)
#define file2 freopen("output.txt","w",stdout)

int main()
{

    file;
    file2;
    int n;
    cin>>n;
    double c,f,x;

    forn(i,n)
    {
        cin>>c>>f>>x;
        double d=2.;

        double a=x/d;
        double b=c/d;
        d+=f;
        b+=x/d;
        while(a>b)
        {
            a=b;
            b+=c/d-x/d;
            d+=f;
            b+=x/d;
           // cout<<b<<endl;
        }
        if(a>b) a=b;
        printf("Case #%d: ",i+1);
        printf("%.7lf\n",a);
    }


}


