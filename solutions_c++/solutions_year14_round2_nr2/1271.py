#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <functional> 
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime>
#define endl '\n'

using namespace std;

#define lli long long int
#define MP make_pair

const int N = (int)(1e5 + 20);
const lli M = 4294967297ll;

int main()
{
ios_base::sync_with_stdio(0);
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif    
	int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq+1 << ": ";
		
		int a, b, k;
		cin >> a >> b >> k;
		vector<lli> cnt(k, 0ll);
		for(int i = 0; i < a; ++i) {
			for(int j = 0; j < b; ++j) {
				int t = i&j;
				if (t < k) cnt[t]++;
			}
		}
		lli ans = 0;
		for(int i = 0; i < k; ++i) ans += cnt[i];
		cout << ans;
		cout << endl;
	}
    return 0;
}