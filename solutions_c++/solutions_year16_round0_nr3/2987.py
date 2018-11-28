#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define F first
#define S second

const int INF = 1000000000;
const int C = 1000000;
const int mda = 1337 +  14664;

vector<pair<long long, vector<long long> > > ans;

int lp[10001000];

vector<int> pr;

long long p(long long x, int k){
    long long y = 0;
    long long d = 1ll;
    vector<int> T;
    long long X = x;
    while (X > 0){
        T.pb(X%2);
        X /= 2;
    }
    for (int i=0; i<T.size(); i++){
        y += T[i] * d;
        d *= k;
    }
    return y;
}

long long D(long long x){
    long long d = 2ll;
    while (1ll*d*d <= x){
        if (x % d == 0)
            return d;
        d++;
    }
    return 1ll;
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #else
        //freopen("encryption.in", "r", stdin);
        //freopen("encryption.out", "w", stdout);
    #endif // LOCAL
//    int N = 10000000;
//    for (int i=2; i<=N; ++i) {
//	if (lp[i] == 0) {
//		lp[i] = i;
//		pr.push_back(i);
//	}
//	for (int j=0; j<(int)pr.size() && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
//		lp[i * pr[j]] = pr[j];
//    }
    int t, n, k;
    cin >> t >> n >> k;
    long long x = (1ll << (n-1)) + 1;
    //cerr<< x << endl;
    for (int i=0; i<k; i++){
        while (1){
            int f = 1;
            vector<long long> R;
            for (int j=2; j<=10; j++){
                long long c = p(x, j);
                //cerr << c << ' ';
                long long del = D(c);
                //cerr << del << endl;
                if (del == 1){
                    f = 0;
                    break;
                }
                R.pb(del);
            }
            //return 0;
            if (f){
                //cerr << x << endl;
                ans.pb(mp(x, R));
                x+=2;
                break;
            }
            x += 2;
        }
    }
    cout << "Case #1:" << endl;
    for (int i=0; i<k; i++){
        long long x = ans[i].F;
        //cerr << x << endl;
        string s = "";
        while (x > 0){
            if (x % 2) s += '1';
            else
                s += '0';
            x /= 2;
        }
        reverse(s.begin(), s.end());
        cout << s << " ";
        for (int j=0; j<ans[i].S.size(); ++j)
            cout << ans[i].S[j] << ' ';
            cout << endl;
    }
    return 0;
}
