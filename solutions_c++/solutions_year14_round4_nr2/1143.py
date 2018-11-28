#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <utility>

using namespace std;

#define MAXN 1024
#define INF 2000000000
int T, N;
int A[MAXN];
int up[MAXN][MAXN];
int down[MAXN][MAXN];

int brute() {
    int ret = INF;
    for(int mask = 0; mask < (1 << N); mask++) {
        vector<int> L;
        vector<int> R;
        for(int i = 0; i < N; i++)
            if((mask & (1 << i)) == 0)
                L.push_back(i);
            else
                R.push_back(i);
        int cost = 0;
        int sz = (int)L.size();
        for(int i = 0; i < sz; i++)
            for(int j = i + 1; j < sz; j++)
                if(A[L[i]] > A[L[j]])
                    cost++;
        for(int i = 0; i < N - sz; i++)
            for(int j = i + 1; j < N - sz; j++)
                if(A[R[i]] < A[R[j]])
                    cost++;
        for(int i = 0; i < sz; i++)
            for(int j = 0; j < N - sz; j++)
                if(L[i] > R[j])
                    cost++;
//        if(cost == 6)
//            cerr << endl;
        ret = min(ret, cost);
    }
    return ret;
}

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	
	cin >> T;
	for(int t = 1; t <= T; t++) {
        cin >> N;
        for(int i = 0; i < N; i++)
            cin >> A[i];
        
        int ans = brute();
        
//        for(int i = 0; i < N; i++) {
//            up[i][i] = 0;
//            for(int j = i + 1; j < N; j++) {
//                up[i][j] = up[i][j - 1];
//                if(A[i] > A[j])
//                    up[i][j]++;
//            }
//        }
//        
//        for(int i = 0; i < N; i++) {
//            down[i][N] = 0;
//            for(int j = N - 1; j > i; j--) {
//                down[i][j] = down[i][j + 1];
//                if(A[i] < A[j])
//                    down[i][j]++;
//            }
//        }
//        
//        int ans = INF;
//        for(int i = -1; i < N; i++) {
//            int cost = 0;
//            for(int j = 0; j < i; j++) {
//                cost += up[j][i];
//            }
//            
////            if(i >= 0) {
////                int pmax = 0;
////                for(int j = 1; j <= i; j++)
////                    if(A[j] > A[pmax])
////                        pmax = j;
////                cost += down[pmax][i + 1];
////            }
//            
//            for(int j = i + 1; j < N; j++) {
//                cost += down[j][j + 1];
//            }
//            ans = min(ans, cost);
//        }
        
        cout << "Case #" << t << ": " << ans << '\n';
	}
	
	return 0;
}
