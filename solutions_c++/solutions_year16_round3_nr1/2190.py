#include <iostream>
#include <queue>
using namespace std;

typedef pair<int, char> pic;
priority_queue<pic> q;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin >> t;
	for(int z = 0; z != t; ++z) {
		int n, temp, total = 0;
		cin >> n;

		q = priority_queue<pic>();
		for(int i = 0; i != n; ++i) {
			cin >> temp;
			total += temp;
			q.push({temp, char('A' + i)});
		}

		cout << "Case #" << (z + 1) << ": ";
		while(!q.empty()) {
			pic s1, s2;

			s1 = q.top();
			q.pop();
			cout << s1.second;
			if(s1.first > 1)
				q.push({s1.first - 1, s1.second});
            --total;

			if(!q.empty() && total != 2) {
				s2 = q.top();
				q.pop();
				cout << s2.second;
				if(s2.first > 1)
					q.push({s2.first - 1, s2.second});
                --total;
			}
			cout << " ";
		}
		cout << "\n";
	}

	return 0;
}
