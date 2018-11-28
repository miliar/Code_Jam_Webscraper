
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

#define all(v)				((v).begin()), ((v).end())
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


int v[10];
bool ch()
{
    for(int i = 0; i < 10; i++)
        if(v[i] == 0) return 1;
    return 0;
}

void f(int n)
{
    while (n)
    {
        int x = n % 10;
        n /= 10;
        v[x] = 1;
    }
}

int main ()
{
    freopen("/Users/KhalidRamadan/Desktop/input.txt","r",stdin);
    freopen("/Users/KhalidRamadan/Desktop/output.txt","w",stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        clr(v, 0);
        int n, tot = 0, ans = 0;
        cin >> n;
        if(n == 0)
        {
            cout << "Case #" << T << ": ";
            cout << "INSOMNIA" << endl;
        }
        else {
            while (ch())
            {
                tot += n;
                f(tot);
                ans ++;
            }
            cout << "Case #" << T << ": ";
            cout << tot << endl;
        }
    }
}
