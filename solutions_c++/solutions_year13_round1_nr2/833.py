#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

int main(){
    int T;

    cin >> T;
    for(int x=1;x<=T;x++){
        int e,r,n;
        cin >> e >> r >> n;
        vector<int> v(n);

        for(int i=0;i<n;i++) cin >> v[i];

        vector<vector<int> > dp(n+1, vector<int>(e+1, -1));
        
        dp[0][e] = 0;

        for(int i=0;i<n;i++){
            for(int j=0;j<=e;j++){
                if(dp[i][j] == -1) continue;
                for(int k=0;k<=j;k++){
                    int nextE = j - k + r;
                    int G = k * v[i];

                    if(nextE > e) nextE = e;

                    dp[i+1][nextE] = max(dp[i+1][nextE], dp[i][j] + G);
                }
            }
        }
        int ret = -1;
        for(int i=0;i<=e;i++){
            ret = max(ret, dp[n][i]);
        }
        printf("Case #%d: %d\n", x, ret);
    }
}
