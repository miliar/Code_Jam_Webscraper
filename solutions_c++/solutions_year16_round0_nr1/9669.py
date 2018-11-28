/*
 *
 * Copyright(c) 2016 Taikai Takeda <297.1951@gmail.com> All rights reserved.
 *
 */
//include
//------------------------------------------
#include <bits/stdc++.h>
using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for(int i=(b-1);i>=(a);--i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const int MOD = 1000000007;

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))


//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

ll solve(ll n){
    if (n == 0)
        return 0;

    int count = 0;
    vector<int> c(10,0);
    ll nn = n;

    while(count < 10){
        ll _nn = nn;
        while(_nn > 0){
            int d = _nn % 10;
            _nn /= 10;
            if(c[d] == 0){
                c[d]++;
                count++;
            }
        }
        nn += n;
    }

    return nn - n;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;

    REP(i,t){
        ll n,ans;
        cin >> n;
        ans = solve(n);
        cout << "Case #" << i+1 << ": " << (ans>0?to_string(ans):"INSOMNIA") << endl;
    }
    return 0;
}
