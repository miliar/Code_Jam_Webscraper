#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;


string a, b;
vector<string> strings;

int minn(int a, int b) { return (a < b) ? a : b; }


int abs(int a) { return (a<0) ? -a : a; }

int dp[101][101];

#define inf 9999999

int ed(int i, int j) {
	// cout << ";;;; " << i << " " << j << endl;
	
	if (i < 0 || j < 0) return inf;
    if(i == 0 && j == 0) {
    	// cout << "yis " << 
    	return (a[i]==b[j]) ? 0 : inf;
    }
    if(dp[i][j] != -1) return dp[i][j];
    if(a[i] != b[j]) return inf;
    int m = inf;
    
    m = minn(m, ed(i-1, j-1));
    m = minn(m, ed(i, j-1) + 1);
    m = minn(m, ed(i-1, j) + 1);
    // cout << i << " " << j << " " << m << endl;
    return dp[i][j] = m;
}


int main() {
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; ++kase) {

		int n;
		cin >> n;
		// for (in ti = 0; i < n; ++i) {
		// 	cin >> a;
		// 	strings.push_back(a);
		// }

		cin >> a >> b;

		for(int i = 0; i < 101; ++i)
            for(int j = 0; j < 101; ++j)
                dp[i][j] = -1;

        int movs = ed(a.size()-1, b.size()-1);

		if (movs > 99999)
			printf("Case #%d: Fegla Won\n", kase);
		else
			printf("Case #%d: %d\n", kase, movs);
		
	}
	return 0;
}