#include <iostream>
using namespace std;
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <set>
#include <ctime>
#include <stack>
#include <list>
#include <cassert>
#include <iomanip>
#include <deque>
#include <sstream>
#include <fstream>
typedef pair<int,int> pii;
#define rep(i,j,n) for(i=j;i<n;i++)
#define pb push_back
#define ff first
#define ss second 
#define lli long long int
#define get getchar

inline int scan() {
    int n=0,s=1;
    char p=get();
    if(p=='-')  s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-') p=get();
    if(p=='-') s=-1,p=get();
    while(p>='0'&&p<='9') { n = (n<< 3) + (n<< 1) + (p - '0'); p=get(); }
    return n*s;
}
int main() {
        
    ios::sync_with_stdio(false);
    
    //clock_t start = std::clock();
    freopen ("inp.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    //cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;
    cout << fixed << setprecision(10);
    int t; cin >> t;
    string nnn = "IMPOSSIBLE";
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
        int n,k;
        cin >> n >> k;
        long double prob = 0;
        vector <long double> gg(n);

        for (int i = 0; i < n; i++) {
            cin >> gg[i];
        }
        sort(gg.begin(),gg.end());
        vector <long double> tmp(k);
        for (int i = 0; i <= k; i++) {
            int cnt = 0;
            for (int j = 0; j < i; j++) {
                tmp[j] = gg[j];
                cnt++;
            }
            for (int j = n-1; cnt < k; j--) {
                tmp[cnt] = gg[j];
                cnt++;
            }

            sort(tmp.begin(),tmp.end());

            long double dp[2][k+2];

            for (int i1 = 0; i1 < 2; i1++)
                for (int i2 = 0; i2*2 < k+2; i2++)
                        dp[i1][i2] = 0;

            dp[0][0] = 1;
            for (int id = 0; id < k; id++) {
                for (int head = 0; head*2 <= k; head++) {
                    long double cur = 0;
                    if (head)
                    cur += dp[0][head-1]*tmp[id];
                    cur += dp[0][head]*(1-tmp[id]);
                    dp[1][head] = cur;
                }
                for (int ii = 0; ii < k+2; ii++)
                    dp[0][ii] = dp[1][ii];
            }
            if (prob < dp[0][k/2])
                prob = dp[0][k/2];
        }
        cout << prob << endl;
    }
    
    
    return 0;
        
}