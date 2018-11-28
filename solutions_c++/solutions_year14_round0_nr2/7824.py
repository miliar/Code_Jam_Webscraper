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

int main(int argc, char *argv[])
{
    int T; cin >> T;
    for (int ca = 1; ca <= T; ca++) {
	double c, f, x;
	cin >> c >> f >> x;
	double speed  = 2;
	double ans = 100000;
	double elapse = 0;
	while (elapse < ans) {
	    ans = min(ans, elapse + x/speed);
	    elapse += c / speed;
	    speed += f;
	}
	cout << "Case #" << ca <<": ";
	cout.precision(10);
	cout << ans << "\n";
    }
    return 0;
}

