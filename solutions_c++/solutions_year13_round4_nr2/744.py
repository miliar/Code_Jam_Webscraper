/* Divanshu Garg */
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
#include <cassert>
#include <fstream>

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
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define MAX(a,b) ((a)>(b)?(a):(b))
int ABS(int a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second
#define piii pair<int,pii>

/* Relevant code begins here */

int main() {

    // freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin.sync_with_stdio(false);


    ill t,tests=1,i;
    cin >> t;

    while ( t-- ) {

        ill n,p;
        cin >> n >> p;

        ill temp = (1LL<<(n-1));

        ill plus = 0;
        ill ans = 0;
        ill could = 0;
        ill where = n-2;
        if ( p <= temp ) goto done;
        if ( p == (1LL<<n) ) {
            could = (1LL<<n)-1;
            goto done;
        }

        could = 2;
        plus = 4;
        temp = temp | (1LL<<where) ;
        while ( p > temp ) {
            could += plus;
            plus *= 2LL;
            where--;
            temp |= (1LL<<where);
        }

        done:


        ill best = 0;
        temp = (1LL<<n);
        if ( temp == p ) {
            best = (1LL<<n)-1;
            goto end;
        }
        if ( p == 1 ) goto end;

        best = (1LL<<(n-1));
        where = n-2;
        temp = 3;
        plus = 4;
        while ( p > temp ) {
            best |= ((1LL)<<where);
            where--;
            temp += plus;
            plus *= 2LL;
        }

        end:        

        cout << "Case #" << tests << ": ";
        cout << could << " " << best;
        cout << endl;
        tests++;

    }

    return 0;
}