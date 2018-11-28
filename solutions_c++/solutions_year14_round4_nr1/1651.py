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
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;

#define INF 1000000000
#define EPS (double)1e-9
#define MOD 1000000007
#define PI 3.14159265358979328462
int s[10005];
int main(int argc, char *argv[])
{
    int T; cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        int n, cap; cin >> n >> cap;
        rep(i,1,n) scanf("%d", s+i);
        sort(s+1, s+n+1);
        int ans = 0;
        int i, j;
        j = n;
        for (int i = 1; i <= j; i++) {
            while (i < j && s[i]+s[j] > cap) {
                j--; ans++;
            }
            if (i == j) {
                ans++;break;
            } else {
                ans++;j--;
            }
            
        }
        cout << "Case #" << ca << ": ";
        cout << ans << endl;
    }
    return 0;
}

