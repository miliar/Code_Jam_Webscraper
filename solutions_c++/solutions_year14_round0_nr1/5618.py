/*
 * Author:  Plumrain
 * Created Time:  2014-04-12 20:07
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <cctype>
#include <ctime>
#include <utility>

using namespace std;

#define clr(x,y) memset(x, y, sizeof(x))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(v) ((int)(v).size())
#define all(t) t.begin(),t.end()
#define INF 999999999999999999
#define zero(x) (((x)>0?(x):-(x))<eps)
#define repf(i, a, b) for(int i = (a); i <= (int)(b); i ++)
#define repd(i, a, b) for(int i = (a); i >= (int)(b); i --)
#define out(x) cout<<#x<<":"<<(x)<<endl
#define tst(a) cout<<a<<" "
#define tst1(a) cout<<#a<<endl
#define CINBEQUICKER std::ios::sync_with_stdio(false)

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;

const double eps = 1e-10;
const double PI = atan(1.0)*4;
const int inf = 2147483647 / 2;

template <class T> void chmin(T &t,T x){if (x < t) t = x;}
template <class T> void chmax(T &t,T x){if (x > t) t = x;}

int an[2][5][5];

pii gao (int p){
    pii ret;
    repf (i, 1, 4) repf (j, 1, 4) if (an[0][i][j] == p) ret.x = i;
    repf (i, 1, 4) repf (j, 1, 4) if (an[1][i][j] == p) ret.y = i;
    return ret;
}

int main()
{
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("a.out","w",stdout);
//    std::ios::sync_with_stdio(false);
    int T, cas = 0;
    scanf ("%d", &T);
    while (T--){
        int tn[2];
        repf (t, 0, 1){
            scanf ("%d", &tn[t]);
            repf (i, 1, 4) repf (j, 1, 4) scanf ("%d", &an[t][i][j]);
        }
        
        vi ans;
        repf (i, 1, 16){
            pii tmp = gao (i);
            if (tmp.x == tn[0] && tmp.y == tn[1]) ans.pb (i);
        }

        printf ("Case #%d: ", ++ cas);
        if (!sz(ans)) printf ("Volunteer cheated!\n");
        else if (sz(ans) > 1) printf ("Bad magician!\n");
        else printf ("%d\n", ans[0]);
    }
    return 0;
}
