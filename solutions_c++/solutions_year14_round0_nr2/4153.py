#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2 * acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second
#define file freopen("input.txt","r",stdin)
#define file2 freopen("output.txt", "w",stdout)
using namespace std;
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;
#define time nlnlkjnlhkjbk
#define inf 100000000000
#define mod 1000000007
#define N 50005
int main(){
    file;
    file2;
    double ans;
    double c, f, x;
    double time, m_time;
    double cur;
    int t;
    cin>>t;
    rep(q, t){
    scanf("%lf%lf%lf",&c,&f,&x);
    cur = 2.0;
    ans = x / cur;
    time = 0;
    rep(i, 1000000){
        time += c / cur;
        cur += f;
        ans = min(ans, time + x / cur);
        }
        printf("Case #%d: %.9lf\n", q + 1, ans);
    }
}
