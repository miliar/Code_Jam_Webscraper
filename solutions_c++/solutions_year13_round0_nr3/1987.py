#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <complex>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl

vector<ill> v;

bool ispalin(ill n) {
    ill temp = n;
    ill rev = 0;
    while ( n > 0 ) {
        rev = rev*10 + n%10;
        n /= 10;
    }
    if ( rev == temp ) return true;
    return false;
}

#define MAX 10000005
void pre() {
    ill i;
    F(i,1,MAX) {
        if ( ispalin(i) ) {
            ill x = i*i;
            if ( ispalin(x) ) {
                v.pb(x);
            }
        }
    }
}

int main() {
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    pre();
    int t,i,T;
    cin >> T;
    F(t,1,T+1) {
        ill a,b;
        cin >> a >> b;
        cout << "Case #" << t << ": " << upper_bound(v.begin(),v.end(),b)-lower_bound(v.begin(),v.end(),a) << endl;        
    }
}