#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int table[9] = { 1, 2, 3, 3, 4, 4, 5, 5, 5 };
int ans;

void calc(vector<int> v, int cnt) {
	if (v.front() >= 4) {
		ans = min(cnt + v.front(), ans);
		pop_heap(v.begin(), v.end());
		int cur = v.back();
		int cur1, cur2;
		for (int i = 2; i <= cur / 2; ++i) {
			cur1 = i;
			cur2 = cur - i;
			vector<int> v2(v);
			v2.pop_back();
			v2.push_back(cur1);
			push_heap(v2.begin(), v2.end());
			v2.push_back(cur2);
			push_heap(v2.begin(), v2.end());
			calc(v2, cnt + 1);
		}
	} else {
		ans = min(cnt + v.front(), ans);
	}
}

int main() {
	int T;
	cin >> T;
	int N;
	int val;
	int maxval;
	for (int t = 1; t <= T; ++t) {
		cin >> N;
		vector<int> v;
		maxval = 0;
		for (int i = 0; i < N; ++i) {
			cin >> val;
			if (val > maxval)
				maxval = val;
			v.push_back(val);
		}
		ans = maxval;
		make_heap(v.begin(), v.end());
		calc(v, 0);

		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;

}

//int main() {
//	int T;
//	cin >> T;
//	int N;
//	int val;
//	int maxval;
//	for (int t = 1; t <= T; ++t) {
//		cin >> N;
//		vector<int> v;
//		int ans = 0;
//		maxval = 0;
//		int cnt = 0;
//		int underfourmax = 0;
//		for (int i = 0; i < N; ++i) {
//			cin >> val;
//			if (val >= 4) {
//				if (val > maxval)
//					maxval = val;
//				v.push_back(val);
//			} else
//				underfourmax = max(underfourmax, val);
//		}
//		ans = max(maxval, underfourmax);
//		make_heap(v.begin(), v.end());
//		while (v.size()) {
//			ans = min(cnt + v.front(), ans);
//			pop_heap(v.begin(), v.end());
//			int cur = v.back();
//			v.pop_back();
//			int cur1 = cur / 2;
//			int cur2 = cur - cur1;
//			if (cur1 >= 4) {
//				v.push_back(cur1);
//				push_heap(v.begin(), v.end());
//			} else {
//				underfourmax = max(underfourmax, cur1);
//			}
//			if (cur2 >= 4) {
//				v.push_back(cur2);
//				push_heap(v.begin(), v.end());
//			} else {
//				underfourmax = max(underfourmax, cur2);
//			}
//			cnt++;
//		}
//		cout << "Case #" << t << ": " << ans << endl;
//	}
//	return 0;
//
//}

//const int MAXN = 1003;
//int array[MAXN];
//int main() {
//	int T;
//	int t;
//	int N;
//	int ans;
//	cin >> T;
//	for (int t = 1; t <= T; ++t) {
//		cin >> N;
//		for (int i = 0; i < N; ++i) {
//			cin >> array[i];
//		}
//
//		array[N] = 0;
//		N = N + 1;
//		ans = 0;
//		sort(array, array + N + 1);
//		int start = 1;
//		int level = 0;
//		while (start < N) {
//			if (array[N - 1] >= 4) {
//				ans++;
//				start--;
//				array[start] = array[N - 1] / 2;
//				array[N - 1] -= array[start];
//				int i = start;
//				while (i + 1 < N && array[i] > array[i + 1]) {
//					swap(array[i], array[i + 1]);
//				}
//				i = N - 1;
//				while (i - 1 >= start && array[i] < array[i - 1]) {
//					swap(array[i], array[i - 1]);
//				}
//			}
//			ans += array[start] - level;
//			level = array[start];
//			start += 1;
//			while (start < N && array[start] == level) {
//				start++;
//			}
//		}
//
//		cout << "Case " << t << ": " << ans << endl;
//
//	}
//
//}
