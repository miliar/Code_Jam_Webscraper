#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

struct Data {
	Data(char c, int count) : c(c), count(count) {}
	char c;
	int count;
};

bool operator < (const Data& lhs, const Data& rhs) {
	if (lhs.count != rhs.count) return (lhs.count < rhs.count);

	return (lhs.c < rhs.c);
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		cin >> n;
		priority_queue<Data, vector<Data>> pq;
		int sum = 0;

		for (int l = 0; l < n; ++l) {
			int count;
			cin >> count;
			pq.push(Data('A' + l, count));
			sum += count;

		}

		vector<string> res;

		while (!pq.empty()) {

			string s;
			auto data = pq.top();
			pq.pop();
			sum--;
			s += data.c;

			data.count--;

			if (data.count > 0) {
				pq.push(data);
			}

			if (!pq.empty()) {
				bool ok = true;
				auto tmp = pq;
				if (tmp.size() > 1) {
					if (tmp.top().count == 1) tmp.pop();
					else {
						auto d = tmp.top();
						tmp.pop();
						d.count--;
						tmp.push(d);
					}

					if (2 * tmp.top().count >= sum) ok = false;
				}

				if (ok) {
					auto x = pq.top();
					s += x.c;
					pq.pop();
					sum--;
					x.count--;
					if (x.count > 0) pq.push(x);
				}
			}

			res.push_back(s);
		}

		cout << "Case #" << i << ":";

		for (auto& v : res) {
			cout << " " << v;
		}

		cout << endl;

	}

	return 0;
}
