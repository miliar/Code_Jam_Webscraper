#include <cstring>
#include <string>
#include <string.h>
#include <map>
#include <deque>
#include <iterator>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <list>

using namespace std;

#define FST first
#define SND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef long double LD;

typedef stringstream SS;
typedef pair<int,string> PIS;
typedef pair<int ,int> PII;
typedef vector<PIS> VPIS;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

#define ALL(x) (x).begin(),(x).end()
#define FOR1(i,n) for(int i=0;i<(n);i++)
#define FOR2(i,n,m)for(int i=n;i<=(m);++i)
#define FORD(i,n,m) for(int i=n;i>=(int)(m);--i)
#define FORI(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define SIZE(a) ((int)((a).size()))

#define Fname "b"

int main()
{
    // ---------------------------
        freopen(Fname ".in","rt",stdin);
        freopen(Fname ".out","wt",stdout);
   // ------------------------------
int T;
cin>>T;
FOR1(nn,T)
{
    int a,b,k,mx,s,c=0;
    cin>>a>>b>>k;
    if(a>=b)
    {
        mx=a;
        s=b;
    }
    else
    {
        mx=b;
        s=a;
    }
    FOR1(i,mx)
    {
        FOR1(j,s)
          {
              if((i&j)<k)
                c++;
          }
    }
    cout<<"Case #"<<nn+1<<": "<<c<<endl;
}

}
