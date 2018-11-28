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

#define Fname "a2"

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
     VI v;
int f,s,c,a[4],b[4],j,k,arr[4][4],brr[4][4];

     cin>>f;
     for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)

            cin>>arr[j][k];
     }
     cin>>s;
     for(j=0;j<4;j++)
     {
         for(k=0;k<4;k++)
            cin>>brr[j][k];
     }
     for(j=0;j<4;j++)
     {
         a[j]=arr[f-1][j];
     }
     for(j=0;j<4;j++)
     {
         b[j]=brr[s-1][j];
     }
     sort(a,a+4);
     sort(b,b+4);

        set_intersection(a,a+4,b,b+4,back_inserter(v));
c=int(v.size());
 cout<<"Case #"<<i+1<<":";
 if(c==1)
    cout<<" "<<v[0]<<endl;
    else if(c>1)
        cout<<" Bad magician!"<<endl;
    else
        cout<<" Volunteer cheated!"<<endl;

     }
 }

