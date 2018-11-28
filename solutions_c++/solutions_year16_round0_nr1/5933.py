#include <iostream>
#include <cstring>

using namespace std;

int main() {
	int n;
	cin >> n;
	for(int test = 1; test <= n; test++) {
		cout << "Case #" << test << ": ";
		int x_;
		cin >> x_;
		if (x_ == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int mark[10];
		memset(mark, 0, sizeof mark);
		int sum = 0;
		for(int x = x_; sum < 10; x += x_) {
			for(int i=x; i; i/=10) {
				int j = i % 10;
				if (mark[j] == 0)
					sum ++;
				mark[j] = 1;
			}
			if (sum == 10)
				cout << x << endl;
		}

	}
}
