
#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>

using namespace std;

#define all(v)				((v).rbegin()), ((v).rend())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)


typedef long long         ll;
const ll OO = 1e9;

#define pb					push_back
#define MP					make_pair
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
#define ff  first
#define ss second
#define mod(a,b)  (a%b+b)%b
typedef long double   	  ld;
typedef vector<int>       vi;
typedef vector<double>    vd;
typedef vector< vi >      vvi;
typedef vector< vd >      vvd;
typedef vector<string>    vs;




int main ()
{
    //        freopen("/Users/KhalidRamadan/Desktop/input.txt","r",stdin);
    //        freopen("/Users/KhalidRamadan/Desktop/output.txt","w",stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        int n;
        int tot = 0;
        cin >> n;
        vector< pair<int, char> > a(n);
        for(int i = 0; i < n; i++)
        {
            cin >> a[i].first;
            a[i].second = 'A' + i;
            tot += a[i].first;
        }
        sort(all(a));
        cout << "Case #" << T << ":";
        int mx1 = 0, mx2 = 0;
        while (a[0].first != 0)
        {
            a[0].first --;
            tot --;
            mx1 = max(a[0].first - 1,a[1].first);
            mx2 = max(a[0].first, a[1].first - 1);
            if(n >= 2) mx2 = max(mx2, a[2].first);
            if(2 * mx1 <= tot - 1)
            {
                a[0].first --;
                tot--;
                cout << " " << a[0].second << a[0].second;
            }
            else if(2 * mx2 <= tot - 1)
            {
                a[1].first --;
                tot --;
                cout << " " << a[0].second << a[1].second;
            }
            else
            {
                cout << " " << a[0].second;
            }
            sort(all(a));
        }
        cout << endl;
    }
}
