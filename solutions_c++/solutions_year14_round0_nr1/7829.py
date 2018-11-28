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
int a[4][4], b[4][4];
int main(int argc, char *argv[])
{
    int T; cin >> T;
    for (int ca = 1; ca <= T; ++ca) {
	int r1, r2; cin >> r1;
	for (int i = 0; i < 4; i++)
	    for (int j = 0; j < 4; j++) cin >> a[i][j];
	cin >> r2;
	for (int i = 0; i < 4; i++)
	    for (int j = 0; j < 4; j++) cin >> b[i][j];
	int c[20] = {0};
	memset(c, 0, sizeof(c));
	for (int i = 0; i < 4; i++)
	    c[a[r1-1][i]] = 1;
	int repe = 0, num;
	for (int i = 0; i < 4; i++)
	    if (c[b[r2-1][i]]) {
		repe++;
		num = b[r2-1][i];
	    }
	cout << "Case #" << ca << ": ";
	if (repe == 1)
	    cout << num;
	else if (repe == 0)
	    cout << "Volunteer cheated!";
	else
	    cout << "Bad magician!";
	cout << endl;
    }
    return 0;
}

