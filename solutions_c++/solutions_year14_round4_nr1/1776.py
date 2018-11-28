/*
 * Author:  Plumrain
 * Created Time:  2014/5/31 22:38:09
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
#define INF 999999999999999999LL
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

bool v[100005];
int an[100005];

int search (int l, int r, int t, int num){
    int ret = 0;
    while (l <= r){
        int mid = (l + r) >> 1;
        if (t + an[mid] <= num) ret = mid, l = mid + 1;
        else r = mid - 1;
    }
    return ret;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
//    std::ios::sync_with_stdio(false);
    int T, cas = 0;
    cin >> T;
    while (T--){
        int n, num;
        cin >> n >> num;
        repf (i, 0, n-1) cin >> an[i];
        sort (an, an+n);
        int ans = n, pos = n;
        clr (v, 0);
        repf (i, 0, n-1) if (!v[i]){
            if (an[i] * 2 > num) break;
            int j = search (0, pos-1, an[i], num);
            if (j <= i) break;
            v[j] = 1; -- ans; pos = j;
        }
        printf ("Case #%d: %d\n", ++ cas, ans);
    }
    return 0;
}
