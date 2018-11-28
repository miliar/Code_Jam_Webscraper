#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <climits>
#include <cmath>
#include <map>
#include <queue>
#include <deque>

using namespace std;

int main() {
	int cases;
	//freopen("inp.txt", "r", stdin);
	//freopen("op.txt", "w", stdout);
	scanf("%d", &cases);
	for(int t = 1; t <= cases; ++t) {
		int smax;
		cin >> smax;
		vector <int> arr;
		string inp;
		cin >> inp;
		for(int i = 0; i < inp.size(); ++i) arr.push_back(inp[i] - '0');
		int a = 0, already_added = 0;		
		int n = arr.size();
		int pre[n + 1];
		pre[0] = arr[0];
		for(int i = 1; i < n; ++i) pre[i] = pre[i - 1] + arr[i];
		//for(int i = 0; i < n; ++i) cout << pre[i] << ' ';
		//cout << '\n';
		for(int i = 1; i < n; ++i) {
			//cout << "I: " << i << " already: " << already_added << '\n';
			if(arr[i] == 0) continue;
			if(pre[i - 1] + already_added < i) {								
				a += i - (pre[i - 1] + already_added);
				already_added += i - (pre[i - 1] + already_added);
			}
		}
		if(n == 1) a = (arr[0] == 0) ? 1 : 0;
		cout << "Case #" << t << ": " << a << '\n';
	}
}
