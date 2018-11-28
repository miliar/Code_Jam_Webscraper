#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <sstream>
using namespace std;

#define DB(x) cerr<<#x<<"="<<x<<" "
#define DBN(x) cerr<<#x<<"="<<x<<"\n"
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define sqr(x) ((x)*(x))
#define sz(x) ((int)(x).size())
#define clr(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define mp make_pair

#define lson x+x,l,y
#define rson x+x+1,y+1,r

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<long long, long long> PLL;

#define INF 1000000000
#define EPS (double)1e-9
#define MOD 1000000007
#define PI 3.14159265358979328462

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++)
    {
        string s;
        int n; cin >> n;
        cin >> s;
        int acc = 0, need = 0;
        for (int j = 0; j < s.size(); j++)
            if (acc >= j) {
                acc += s[j]-'0';
            } else {
                need += j-acc;
                acc = j;
                acc += s[j]-'0';
            }
        cout << "Case #" << ca << ": " << need << endl;
    }
    return 0;
}

