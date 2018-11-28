/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define f first
#define s second

LL getRank(LL k, int n) {
    if(k==1)    return 0;
    k>>=1;
    n--;
    LL rank = 1LL;
    while(k>1 && n>0) {
        k>>=1;
        rank<<=1;
        rank++;
        n--;
    }
    while(n-->0) {
        rank<<=1;
    }
    return rank;
}

LL getBestRank(LL k, int n) {
    LL mx = 1LL<<n;
    k = mx-k+1;
    LL rank = 0;
    while(k>1 && n>0) {
        k>>=1;
        n--;
    }
    while(n-->0) {
        rank<<=1; rank++;
    }
    return rank;
}

int main(){
    int t;
    cin>>t;
    FF(kase,1,t+1){
        cout<<"Case #"<<kase<<": ";
        LL p;
        int n;
        cin>>n>>p;
        p--;
        LL lft = 1LL;
        LL rgt = 1LL<<n;
        LL md = lft;
        while(rgt-lft>1) {
            md = (lft+rgt)/2;
            LL rank = getRank(md,n);
            if(rank > p)    rgt = md-1;
            else            lft = md;
        }
        md = lft;
        while(lft<=rgt) {
            if(getRank(lft,n) <= p)   md = lft;
            else    break;
            lft++;
        }
        cout<<md-1<<" ";
        
        
        // ****************** //

        lft = 1LL;
        rgt = 1LL<<n;
        md = lft;
        while(rgt-lft>1) {
            md = (lft+rgt)/2;
            LL rank = getBestRank(md,n);
            if(rank > p)    rgt = md-1;
            else            lft = md;
        }
        md = lft;
        while(lft<=rgt) {
            if(getBestRank(lft,n) <= p)   md = lft;
            else    break;
            lft++;
        }
        cout<<md-1<<endl;
    }
    return 0;
}
