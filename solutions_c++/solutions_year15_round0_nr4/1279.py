
#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef set<int> sI;
typedef set<pI> spI;
typedef priority_queue<int> qmax;
typedef priority_queue<int, vector<int>, greater<int> >qmin;
typedef map<int, int>::iterator mI_it;
typedef set<int>::iterator sI_it;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)
#define MP make_pair
#define PB push_back
#define F0(i, n) for( int (i) = 0; (i) < (n); (i)++)
#define F1(i, n) for( int (i) = 1; (i) <= (n); (i)++)
#define zero(i) memset((i),0,sizeof((i)))


int main()
{
    freopen("out.txt","w",stdout);
    freopen("D-small-attempt2.in","r",stdin);
    int t, x, r, c;
    while(cin>>t){
        for(int z = 1; z <= t; z++){
            cin>>x>>r>>c;
            bool ans = true;
            if((r * c) % x != 0) ans = false;
            int p = min(r, c);
            if(p < (x+1)/2) ans = false;
            if(x > 3 && p == (x+1)/2) ans = false;
            cout<<"Case #"<<z<<": ";
            if(ans == false) cout<<"RICHARD"<<endl;
            else cout<<"GABRIEL"<<endl;
        }
    }
    return 0;
}
