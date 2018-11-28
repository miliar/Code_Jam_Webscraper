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
#define file freopen("D-large.in","r",stdin)
#define file2 freopen("doutput.txt","w",stdout)

double a[2000], b[2000];
int main()
{

    file;
    file2;
    int n;
    cin>>n;

    forn(i,n)
    {
        int m;
        cin>>m;
        forn(i,m)
            cin>>a[i];

        forn(i,m)
            cin>>b[i];

        sort(a, a+m);
        sort(b, b+m);

        int j1=m-1, j2=m-1;

         int k1=0;
        int k2=0;
        while(j1>=0 && j2>=0)
            if(a[j1]>b[j2]) j1--, j2--, k1++; else j2--;

        j1=m-1; j2=m-1;
        while(j1>=0 && j2>=0)
            if(a[j1]>b[j2])j1--,k2++; else j1--, j2--;



        cout<<"Case #"<<i+1<<": "<<k1<<' '<<k2<<endl;
    }


}


