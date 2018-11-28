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

#define Fname "bl"

int main()
{
    // ---------------------------
        freopen(Fname ".in","rt",stdin);
        freopen(Fname ".out","wt",stdout);
   // ------------------------------

     int n,i;

    cin>>n;
    for(i=0;i<n;i++)
    {
        double c,f,x,r,mini=0.0,d,t;
        double a1=0.0,a2=0.0;
        cout<<fixed<<setprecision(7);
        cin>>c;
        cin>>f;
        cin>>x;
        r=2.0;
        mini=double(x/r);
        while(mini!=NULL)
        {
        a1=a1+a2;
        a2=double(c/r);

        r=r+f;
        t=double(x/r);
        d=t+a2+a1;
         if(mini<d)
            break;
        else
            mini=d;


        }
        cout<<"Case "<<"#"<<i+1<<": "<<mini<<endl;

    }


}
