#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <numeric>
#include <bitset>

using namespace std;

template<typename T> ostream& operator<<(ostream& os, const vector<T>& v){
    os << "{ ";
    for (typename vector<T>::const_iterator it = v.begin(); it != v.end(); ++it)
        os << '\"' << *it << '\"' << (it + 1 == v.end() ? "" : ", ");
    os << " }";
    return os;
}

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
#define vv(type,w,h,init) vector<vector<type>>(h,vector<type>(w,init))
typedef vector<string> vs;
typedef long long ll;
typedef unsigned uint;
typedef unsigned long ul;
typedef unsigned long long ull;

#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define loop(i,a,b) for(int i=(a); i<(int)(b); i++)
#define rep(i,b) loop(i,0,b)
#define pb push_back
#define mp make_pair

string const resstr[] = { "Impossible", "Possible", "No", "Yes" };

template<typename T> void output(int n, T const & ans){
    printf("Case #%d: ", n);
    cout << ans << endl;
}

void solve(int n){
    double dc, dv, x;
    double v = 2.0;
    cin >> dc >> dv >> x;
    double ans = 0.0;
    while (1){
        double t1 = x / v;
        double t2 = dc / v + x / (v + dv);
        if (t1 < t2){
            ans += x / v;
            break;
        }
        else {
            ans += dc / v;
            v += dv;
        }
    }
    output(n, ans);
}

int main(){
    cout << fixed << setprecision(15);
    int n; cin >> n;
    rep(i, n) solve(i + 1);
}
