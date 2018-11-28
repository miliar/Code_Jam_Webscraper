/*
 * Author:  Plumrain
 * Created Time:  2014/4/26 9:17:02
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
template <class T> int sgn(T x) { return (x > eps) - (x < -eps);}

int ans[45], n, l, ans_num;
vs vbn;
string no = "NOT POSSIBLE";
string an[155], bn[155], cn[155];

int ok(){
    repf (i, 0, n-1) cn[i] = an[i];
    repf (i, 0, l-1) if (ans[i]){
        repf (j, 0, n-1) cn[j][i] = (cn[j][i] == '1' ? '0' : '1');
    }

    vs tmp;
    repf (i, 0, n-1) tmp.pb (cn[i]);
    sort (all(tmp));
    repf (i, 0, sz(tmp)-1) if (tmp[i] != vbn[i]) return 0;
    return 1;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);
//    std::ios::sync_with_stdio(false);
    int T, cas = 0;
    scanf ("%d", &T);
    while (T--){
        scanf ("%d%d", &n, &l);
        repf (i, 0, n-1) cin >> an[i];
        repf (i, 0, n-1) cin >> bn[i];

        vbn.clear(); 
        repf (i, 0, n-1) vbn.pb (bn[i]);
        sort (all(vbn));
        
        clr (ans, 0);
        ans_num = inf;
        repf (i, 0, n-1){
            int cnt = 0;
            repf (j, 0, l-1) ans[j] = 1 - (an[0][j] == bn[i][j]), cnt += ans[j];
            if (ok()) chmin (ans_num, cnt);
        }
        printf ("Case #%d: ", ++ cas);
        if (ans_num == inf) cout << no << endl;
        else cout << ans_num << endl;
    }
    return 0;
}
