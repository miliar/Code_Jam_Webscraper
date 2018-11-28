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
int cn;
cin>>cn;
FOR1(i,cn)
{
    cout<<fixed<<setprecision(7);
    double c,f,x,rate,minmum,sec,b1=0.0,b2=0.0,sum;
    cin>>c;
    cin>>f;
    cin>>x;
    rate =2.0;
    minmum = x/rate;
while(1)
{
    b1=b1+b2;
    b2=c/rate;
    rate = rate + f;
    sec = x/rate;
    sum = b2+sec+b1;
    if(sum>minmum)
        break;
    else
        minmum = sum;
}
cout<<"Case #"<<i+1<<": "<<minmum<<'\n';
}
}
