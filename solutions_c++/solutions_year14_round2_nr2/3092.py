#include<iostream>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<list>
#include <algorithm>
using namespace std;
typedef long long i64;
typedef unsigned long long ui64;

int main()
{
    freopen("in", "r", stdin);
    // freopen("out", "w", stdout);
    i64 T;
    cin >> T;
    string com;
    for (int t = 1; t <= T; ++t) {
	i64 A, B, K;
	cin >> A >> B >> K;
	i64 x = min (A, B);
	i64 y = max (A, B);
	ui64 ans = 0;
	if (x < K) {
	    ans = A*B;
	    cout << "Case #" << t << ": " << ans << endl;
	    continue;
	}
	ans = K*y;
	for (ui64 i = K; i < x; ++i) {
	    ans += K;
	    for (ui64 j = K; j < y; ++j) {
		ui64 aa = i & j;
		if (aa < K)
		    ++ans;
	    }
	}
	cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

