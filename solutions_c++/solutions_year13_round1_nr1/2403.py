#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <math.h>

#define ss stringstream
#define fo(a, b, c) for(a = (b); a < ( c ); a++ )
#define fr(a, b) fo(a, 0, ( b ) )
#define fi(a) fr(i, ( a ) )
#define fj(a) fr (j, ( a ) )
#define fk(a) fr(k, ( a ) )
#define _(a, b) memset(a, b, sizeof( a ) )

using namespace std;

int ni() { int a; cin>>a;  return a;}
char nc() { char a; cin>>a; return a;}
float nf() { float a; cin>>a; return a;}
long long  nll() { long long  a; cin>>a; return a;}

typedef long long ll;
typedef unsigned long long int lli;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{

    lli tt, i, j, k;
    float s;
    lli r, paint, rings, cost;
    lli a, b, c;
    freopen("A-small-attempt2.IN", "r", stdin);
    freopen("A-small.OUT", "w", stdout);

    cin>>tt;
    //cout<<tt<<endl;
    //tt=1;
    fk(tt)
    {
        cin>>r>>paint;
        a = 1; b = 2*r - 1;
        c = -2*paint;
        s = pow((b*b - 4*a*c), 0.5) - b;
        if(s<0)
            s = pow((b*b - 4*a*c), 0.5) + b;
        //cout<<s;
        s = s/(4*a) ;
        rings = (lli)s;
        //if(s-(lli)s==0) rings--;
        cout<<"Case #"<<k+1<<": "<<rings<<endl;
    }
}
