#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
using namespace std;


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	set<int> seen;
	int n;
	cin >> n;
	long long now;
	for (int i = 0; i < n; i++) {
		cin >> now;
		if (now == 0) {
			cout<< "Case #"<< i+1 <<": "<<"INSOMNIA" << endl;
			continue;
		}
		int k = 1;
		long long base = now;
		while (true) {
			if (seen.size() == 10) {
				cout << "Case #" << i + 1<<": "<<now << endl;
				seen.clear();
				break;
			}
			else {
				now = base  * (k);
				long long temp = now;
				while (temp != 0) {
					seen.insert(temp % 10);
					temp = temp / 10;
				}
				k += 1;
			}
		}
	}

	//system("pause");
	return 0;
}