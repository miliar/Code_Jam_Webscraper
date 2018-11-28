#include <map> 
#include <set> 
#include <list> 
#include <cmath> 
#include <ctime> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <cstdio> 
#include <string> 
#include <bitset> 
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <algorithm> 
#define sqr(x) ((x)*(x)) 
#define ABS(x) ((x<0)?(-(x)):(x)) 
#define eps (1e-9) 
#define mp make_pair 
#define pb push_back 
#define Pair pair<int,int> 
#define xx first 
#define yy second 
#define equal(a,b) (ABS(a-b)<eps) 
using namespace std; 
 
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();} 
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; } 
 
int dx[8]={0, 0, 1,-1, 1, 1,-1,-1}; 
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1}; 
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2}; 
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1}; 
 
/////////////////////////////////////////////////////////////////////////////////////////////////////

string testprefix = "A-small-attempt0";

void solveTest() {
    int x;
    int r1, r2;

    cin >> r1;
    map<int, int> m;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
            cin >> x;
            if (i == r1 - 1) m[x]++;
        }
    cin >> r2;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
            cin >> x;
            if (i == r2 - 1) m[x]++;
        }

    int cnt = 0, res;
    for (map<int,int> :: iterator it = m.begin(); it != m.end(); it++) {
        if (it->second == 2) {
            cnt++;
            res = it->first;
        }
    }

    if (cnt == 0)
        printf("Volunteer cheated!\n");
    else if (cnt >= 2)
        printf("Bad magician!\n");
    else
        printf("%d\n", res);
}

int main() {
    freopen((testprefix + ".in").c_str(), "r", stdin);
    freopen((testprefix + ".out").c_str(), "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solveTest();
    }
    return 0;
}
