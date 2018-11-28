//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl;
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
#define MP make_pair
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

LL T;
LL K,C,S;

LL poww(LL a, LL b)
{
    if(b==0) return 1LL;
    if(b==1) return a;
    LL res = poww(a,b/2);
    res *= res;
    if(b%2) res*=a;
    return res;
}

int main() {
    cin >> T;
    FOR(iii,1,T)
    {
        cin >> K >> C >> S;
        LL add = poww(K,C-1);
        cout << "Case #" << iii << ": ";
        for(LL i = 0; i <= K-1; i++)
        {
            cout << i*add + 1 << " ";
        }
        cout << "\n";
    }


  return 0;
}
