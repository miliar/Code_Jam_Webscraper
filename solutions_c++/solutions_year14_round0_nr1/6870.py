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

int T;
cin>>T;
FOR1(nn,T)
 {
     cout<<"Case #"<<nn+1<<": ";
     int choice,arr[4][4],cnt;
     VI arr1,arr2,vi;
     cin>>choice;
     FOR1(r,4)
       FOR1(c,4)
         cin>>arr[r][c];
    FOR1(c,4)
       arr1.push_back(arr[choice-1][c]);

    cin>>choice;
    FOR1(r,4)
       FOR1(c,4)
         cin>>arr[r][c];
    FOR1(c,4)
       arr2.push_back(arr[choice-1][c]);

    sort(arr1.begin(),arr1.end());
    sort(arr2.begin(),arr2.end());

    set_intersection(arr1.begin(),arr1.end(),arr2.begin(),arr2.end(),back_inserter(vi));
    cnt=int(vi.size());
    if (cnt==1)
        cout<<vi[0];
    else if(cnt>1)
        cout<<"Bad magician!";
    else
        cout<<"Volunteer cheated!";
    cout<<endl;
 }

}
