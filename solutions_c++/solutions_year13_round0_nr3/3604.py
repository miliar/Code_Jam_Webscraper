#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <math.h>

#define ss stringstream
#define pb push_back
#define ppb pop_back
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
typedef long long int lli;
typedef vector<int> vi;
typedef vector<string> vs;

bool palin(lli x)
{
    lli n = x;
    lli r = 0;
    while(x>0)
    {
        r = r*10 + (x%10);
        x /= 10;
    }
    return (r==n);
}
int main()
{
    freopen("C-small-attempt0.IN", "r", stdin);
    freopen("C-small.OUT", "w", stdout);
    int n, i, j, tt, a, b;
    int count = 0;
    double k;
    cin>>tt;
    fr(n, tt)
    {
        cout<<"Case #"<<n+1<<": ";
        count = 0;
        cin>>a>>b;
        fo(i,a,b+1)
        {
            if(palin(i))
            {
                k = sqrt(i);
                if((k-(lli)k)==0)
                    if(palin(k))
                        count++;
            }
        }
        cout<<count<<endl;
    }
}
