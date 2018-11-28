#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <fstream>
#include <time.h>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <deque>
#include <map>
using namespace std;
typedef long long ll;
const int N = 26 + 2;
int n;
int arr[N];


int main(int argc, char *argv[]) {
#ifndef ONLINE_JUDGE
	//freopen("myfile.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	while (t--) {
		memset(arr, 0, sizeof arr);
		scanf("%d", &n);
		int s = 0;
		priority_queue<pair<int, int> > q;
		for (int i = 0; i < n; ++i) {
			scanf("%d", arr + i), s += arr[i];
			q.push(make_pair(arr[i], i));
		}
		string str = "";

		while (!q.empty()) {
			pair<int, int> u= q.top();
			q.pop();
			str += ' ';
			str += (u.second + 'A');
			u.first--;
			if(u.first)
				q.push(u);
			--s;
			if (q.size() && q.top().first>s / 2) {
				u = q.top();
				q.pop();
				str += (u.second + 'A');
				u.first--;
				if (u.first)
					q.push(u);
				--s;
				if (q.size())
					assert(q.top().first > s / 2);
			}

		}
		static int cas = 1;
		printf("Case #%d:", cas++);
		printf("%s\n", str.c_str());
	}

		return 0;
}