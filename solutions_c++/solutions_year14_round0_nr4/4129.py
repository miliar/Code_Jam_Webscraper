#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <limits.h>
#include <deque>

using namespace std;

int fn(deque<double> a, double x)
{
	int low = 0;
	int high = a.size() - 1;

	double y = INT_MAX;
	int ind = high;

	while (low <= high) {
		int mid = low + (high - low) / 2;

		if (x < a[mid]) {
			if (a[mid] < y) {
				y = a[mid];
				ind = mid;
			}
			high = mid - 1;
		} else if (x > a[mid]) {
			low = mid + 1;
		}
	}

	return ind;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("out4_Large.txt", "w", stdout);

	int T;

	cin >> T;

	for (int z = 0; z < T; z++) {
	int n;

	cin >> n;

	deque<double> p;
	deque<double> q;

	double a[n];
	double b[n];
	
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a + n);

	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	sort(b, b + n);
	
	for (int i = 0; i < n; i++) {
		p.push_back(a[i]);
	}

	for (int i = 0; i < n; i++) {
		q.push_back(b[i]);
	}

	int naomi = 0;
	int ken = 0;

	for (int i = n - 1; i >= 0; i--) {
		if (q.back() < p.back()) {
			q.pop_front();
			naomi++;
		} else if (q.back() > p.back()) {
			int j = fn(q, p.back());
			q.erase(q.begin() + j);
			ken++;
		}
		p.pop_back();
	}

	int naomi_war = naomi;

	for (int i = 0; i < n; i++) {
		p.push_back(a[i]);
	}

	for (int i = 0; i < n; i++) {
		q.push_back(b[i]);
	}
	
	naomi = 0;
	ken = 0;

	for (int i = 0; i < n; i++) {
		int m = p.size();
		int flag = 0;

		for (int j = 0; j < m; j++) {
			flag += p[j] > q[j] ? 1 : 0;
		}

		if (flag == m) {
			naomi += m;
			break;
		}
			
	//	if (p.back() > q.back()) {
	//		p.pop_back();
	//		q.pop_front();
	//		naomi++;
//		} else if (p.back() < q.back()) {
			p.pop_front();
			q.pop_back();
			ken++;
//		}
	}

	int naomi_d_war = naomi;

	cout << "Case #" << z + 1 << ": " << naomi_d_war << " " << naomi_war << endl;
	}

	return 0;
}	


