#include <cstring>
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
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
        if (fabs(a - b) < eps)
                return 0;
        return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
        if (i < 0 || j < 0 || i >= I || j >= J)
                return false;
        return true;
}

int N;
string vec_to_key(vector<int>& A)
{
    string s(A.size(), '0');
    for (int i = 0; i < A.size(); ++i) {
        if (A[i] != 0) {
            s[i] = '1';
        }
    }
    return s;
}
list<vector<int> > get_neighbor(vector<int> &A)
{
    list<vector<int> > result;
    for (int i = 0; i < A.size(); ++i) {
        vector<int> tmp(A.begin(), A.end());
        for (int j = 0; j <= i; ++j) {
            tmp[j] ^= 1;
        }
        result.push_back(tmp);
    }
    return result;
}
void print_debug(string ct, list<vector<int> >&A)
{
    cout << endl;
    std::cout << ct << " ";
    For(it, A) {
        string k = vec_to_key(*it);
        std::cout << k << " ";
    }
    cout << endl;
}

void bfs(vector<int>& src, vector<int>& dst, int &depth)
{
    if (src == dst) {
        depth = 0;
        return;
    }
    list<vector<int> > queue(1, src);
    map<string, int> visited;
    while (queue.size()) {
        list<vector<int> > layer(queue.begin(), queue.end());
        queue.clear();
        depth += 1;
        while (layer.size()) {
            vector<int> curr = layer.front();
            layer.pop_front();
            list<vector<int> > neighbors = get_neighbor(curr);
            //print_debug("got neighbor", neighbors);
            For(it, neighbors) {
                if (*it == dst) {
                    // stop the depth
                    return;
                }
            }
            For(it, neighbors) {
                string key = vec_to_key(*it);
                if (visited.find(key) == visited.end()) {
                    visited[key] = 1;
                    queue.push_back(*it);
                }
            }
            //print_debug("New search", queue);
        }
    }
}

int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("B-small-attempt1.in","rt",stdin);
        freopen("B-small-attempt1.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("B-large.in","rt",stdin);
        freopen("B-large.out","wt",stdout);
    }
    else {
        freopen("a.txt", "rt", stdin);
    }

    cin>>N;
    rep2(nn,1,N+1) {
        printf("Case #%d: ", nn);
        string original;
        cin >> original;
        vector<int> src(original.size(), 0);
        vector<int> dst(original.size(), 1);
        for (int i = 0; i < original.size(); ++i) {
            if (original[i] == '+') {
                src[i] = 1;
            }
        }
        int depth = 0;
        bfs(src, dst, depth);
        printf("%d", depth);
        cout<<endl;
    }

    return 0;
}
