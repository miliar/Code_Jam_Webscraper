#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <cstring>
#include <limits>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef vector<vector<char> > vcc;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

string nums[]{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
string anums[]{ "ZERO", "XIS", "WTO", "UFOR", "RTHEE", "FIVE", "VESEN", "GHTEI", "ONE", "NINE" };
int vals[]{ 0, 6, 2, 4, 3, 5 ,7, 8, 1, 9 };
int ohwell[]{ 0, 8, 2, 4, 3, 5, 1, 6, 7, 9 };
int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in", "rt", stdin);
        freopen("small.out", "wt", stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in", "rt", stdin);
        freopen("large.out", "wt", stdout);
    }
    else {
        freopen("a.txt", "rt", stdin);
    }
    int NN;
    cin >> NN;
    rep2(nn, 1, NN + 1) {
        printf("Case #%d: ", nn);
    //////////////////start///

        string in;
        cin >> in;
        vector<int> count(26);
        vi result(10);
        rep(i, in.size()) {
            count[in[i] - 'A']++;
        }
        for (int i = 0; i < 10; i++) {
            int value = count[anums[i][0] - 'A'];
            if (value > 0) {
                if (i == 9)
                    value /= 2;
                rep(j, anums[i].size()) {
                    count[anums[i][j] - 'A'] -= value;
                }
                result[vals[i]] = value;
            }
        }
       
        rep(i, 10) {
            rep(j, result[i]) {
                cout << i;
            }
        }
    //////////////////end////
        cout << endl;
    }
    return 0;
}