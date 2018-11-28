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

#define MAXN 100000

int T, N, X;
int A[MAXN];
multiset<int> B;

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	
	cin >> T;
	for(int t = 1; t <= T; t++) {
        cin >> N >> X;
        for(int i = 0; i < N; i++)
            cin >> A[i];
        sort(A, A + N);
        reverse(A, A + N);
        for(int i = 0; i < N; i++)
            B.insert(-A[i]);
        
        int ans = 0;
        for(int i = 0; i < N; i++) {
            if(B.count(-A[i]) == 0)
                continue;
            
            B.erase(B.find(-A[i]));
            multiset<int> :: iterator it = B.lower_bound(-(X - A[i]));
            ans++;
            if(it != B.end()) {
                B.erase(it);
            }
        }
        
        cout << "Case #" << t << ": " << ans << '\n';
	}
	
	return 0;
}
