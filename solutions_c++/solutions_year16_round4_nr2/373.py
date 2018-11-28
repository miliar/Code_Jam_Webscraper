#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define ff first
#define ss second

#ifndef ONLINE_JUDGE
#define dbg(args...)            {debug,args; cerr<<endl;}
#else
#define dbg(args...)
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
	{
	    cerr<<v<<" ";
	    return *this;
	}
} debug;

typedef long double ld;
int n, k;
vector<ld> arr;
vector<ld> vec;

ld memo[256][256];
ld dp(int id, int wins){
    ld &res = memo[id][wins];
    if (res == res) return res;
    if (id == k){
        if (wins * 2 == k) return res = 1.0;
        return res = 0.0;
    }
    res = 0.0;
    res += vec[id] * dp(id + 1, wins + 1);
    res += (1.0 - vec[id]) * dp(id + 1, wins);
    return res;
}

ld prob_tie(){
    memset(memo, -1, sizeof memo);
    ld res = dp(0, 0);
    return res;
}

void solve(){
    cin >> n >> k;
    arr.resize(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    ld res = 0.0;
    sort(arr.begin(), arr.end());
    for (int i = 0; i <= k; i++){
        vec.clear();
        int L = i, R = k - i;
        for (int i = 0; i < L; i++){
            vec.push_back(arr[i]);
        }
        for (int i = n - R; i < n; i++){
            vec.push_back(arr[i]);
        }
        res = max(res, prob_tie());
    }

    cout << fixed << setprecision(10) << res << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
