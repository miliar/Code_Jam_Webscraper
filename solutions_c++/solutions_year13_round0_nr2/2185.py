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

int a[105][105];
int bin[105][105];
int m,n;

bool row(int x) {
    int i;
    F(i,0,m) {
        if ( bin[x][i] == 2 ) return false;
    }
    return true;
}

bool col(int x) {
    int i;
    F(i,0,n) {
        if ( bin[i][x] == 2 ) return false;
    }
    return true;
}

bool f() {
    int i,j;
    F(i,0,n) {
        F(j,0,m) {
            if ( bin[i][j] == 1 ) {
                if ( !row(i) && !col(j) ) {
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,k,T;
    cin >> T;
    F(t,1,T+1) {
        cin >> n >> m;
        F(i,0,n) {
            F(j,0,m) {
                cin >> a[i][j];
                bin[i][j] = 1;
            }
        }
        FD(k,100,1) {
            F(i,0,n) {
                F(j,0,m) {
                    if ( a[i][j] == k ) bin[i][j]=2;
                }
            }
            if ( !f() ) {
                break;
            }
        }
        cout << "Case #" << t << ": " << (k==0?"YES":"NO") << endl;
    }
    return 0;
}