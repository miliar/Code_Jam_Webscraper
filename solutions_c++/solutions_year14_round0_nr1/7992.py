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

#define Fname "a"

int main()
{
    // ---------------------------
        freopen(Fname ".in","rt",stdin);
        freopen(Fname ".out","wt",stdout);
   // ------------------------------

int cval;
cin>>cval;
FOR1(t,cval)
{
    int rval,arr[4][4],a[4],b[4];
    cin>>rval;
    FOR1(i,4)
        FOR1(j,4)
        cin>>arr[i][j];
    FOR1(i,4)
    {
        a[i]=arr[rval-1][i];
    }
    cin>>rval;
    FOR1(i,4)
        FOR1(j,4)
            cin>>arr[i][j];
    FOR1(i,4)
    {
        b[i]=arr[rval-1][i];
    }
    vector<int> v;
    sort(a,a+4);
    sort(b,b+4);
    set_intersection(a,a+4,b,b+4,back_inserter(v));
    if(int(v.size())>1)
    cout<<"Case #"<<(t+1)<<": Bad magician!";
    else if (int(v.size())<1)
        cout<<"Case #"<<(t+1)<<": Volunteer cheated!";
        else
        cout<<"Case #"<<(t+1)<<": "<<v[0];
        cout<<'\n';
}
}
