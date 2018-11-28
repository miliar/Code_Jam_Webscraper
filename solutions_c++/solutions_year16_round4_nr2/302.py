#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n, k;
double p[210];
double dp1[210][210];
vector<int> v;
double dp[210][210][210];

double rec1(int i, int tot) {
    if (i==k) {
        if (tot == k/2) return 1.0;
        else return 0.0;
    }
    if (dp1[i][tot]>=-0.5) return dp1[i][tot];

    double tmp = p[v[i]]*rec1(i+1, tot+1) + (1.0-p[v[i]])*rec1(i+1, tot);

    dp1[i][tot] = tmp;

    return tmp;
}

double solve1() {

    double res = 0.0;

    for (int i=0; i<(1<<n); i++) {
        if (__builtin_popcount(i) == k) {

            v.clear();
            for (int j=0; j<n; j++) if ((1<<j)&i) v.push_back(j);

            for (int j=0; j<n; j++) for (int t=0; t<=n; t++) dp1[j][t] = -1;

            double tmp = rec1(0,0);

            if (res < tmp) {
                res = tmp;
                //for (int j=0; j<v.size(); j++) cout<<v[j]<<" "; cout<<endl;
            }

        }
    }

    return res;

}

double solve(int i, int tot, int cnt) {

    if (i==n) {
        if (tot==k) {
            if (cnt==k/2) return 1.0;
        }
        return 0.0;
    }

    if (dp[i][tot][cnt]>-0.5) return dp[i][tot][cnt];

    double res = solve(i+1, tot, cnt);

    res = max(res, solve(i+1, tot+1, cnt+1)*p[i] + solve(i+1, tot+1, cnt)*(1.0-p[i]));

    dp[i][tot][cnt] = res;

    cout<<i<<" "<<tot<<" "<<cnt<<" "<<res<<" "<<" "<<solve(i+1, tot+1, cnt+1)<<" "<<p[i]<<" "<<solve(i+1, tot+1, cnt)<<" "<<(1.0-p[i])<<endl;

    return res;

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n>>k;
        for (int i=0; i<n; i++) cin>>p[i];

        sort(p, p+n);

        //double res1 = solve1();

        //printf("Case #%d: %.8f\n", cas, res1);

        //for (int i=0; i<=n; i++) for (int j=0; j<=n; j++) for (int t=0; t<=n; t++) dp[i][j][t] = -1.0;

        //res = solve(0, 0, 0);

        double res = 0.0;
        for (int i=0; i<=n; i++) {
            for (int t=0; t<=n; t++) if (i+t==k) {
                v.clear();
                for (int j=0; j<i; j++) v.push_back(j);
                for (int j=0; j<t; j++) v.push_back(n-1-j);

                for (int j=0; j<n; j++) for (int f=0; f<=n; f++) dp1[j][f] = -1;

                res = max(res, rec1(0, 0));
                //cout<<rec1(0,0)<<endl;
            }
        }

        //if (abs(res-res1) > 0.01) cout<<"ERROR"<<endl;

        printf("Case #%d: %.8f\n", cas, res);

    }

    return 0;

}
