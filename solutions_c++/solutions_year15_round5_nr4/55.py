/*
 * dnkywin's template
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

int m, n;

ll e[10000];
ll f[10000];
map<ll,ll> nums;
vi sums;
vi logger;
vi temp;
void solve_case(int test_case) {
    cout << "Case #" << test_case << ": ";
    /* %%% */
    int p;
    cin >> p;
    rep(i, p) cin >> e[i];
    nums.clear();
    sums.clear();

    int allsums = 0;
    rep(i, p){
        cin >> f[i];
        allsums += f[i];
        nums[e[i]] = f[i];
    }
        
    sums.pb(0);
    nums[0]--;

    logger.clear();
    int nsums = 1;
    while(nsums < allsums) {
        auto it = nums.lower_bound(0);
        if (it->second == 0) {
            nums.erase(it);
            continue;
        }
        nsums <<= 1;
        int newnum = it->first;
        logger.pb(newnum);
        for(int i: sums) {
            nums[i + newnum]--;
            temp.pb(i + newnum);
        }
        sums.insert(sums.end(), all(temp));
        temp.clear();
    }
    rep(i, logger.size()) {
        cout << logger[i] << " \n"[i == logger.size() - 1];
    }
}

int main(){
    int T;
    cin >> T;
    rep(tt, T) solve_case(tt + 1);
    return 0;
}

