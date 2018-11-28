#include <iostream>
#include <vector>
#include <map>

using namespace std;
bool alldone(map<int, int> store) {
	int times[10] = {1,2,3,4,5,6,7,8,9,0};
	int count = 0;
	for (int i = 0; i < 10; i++) {
		if (store[times[i]] == 1) {
			count++;
		}
	}
	return count == 10 ? true : false;
}
int process(int n) {
	bool done = false;
	map<int, int> store;
	int ret = 0;
	int count = 0;
	int p = n;
	int idx = 0;
	while (1) {
		while (p) {
			int r = p % 10;
			p = p / 10;
			store[r] = 1;
		}
		if (alldone(store)) {
			done = true;
			break;
		}
		if (n == 0) {
			ret = -1;
			break;
		}
		idx++;
		p = n * idx;
		ret = p;
	}
	return ret;
}

int main() {
	int N;
	scanf("%d",&N);
	int cases = 0;
	while (N--) {
		cases++;
		int number;
		cin >> number;
		int ret = process(number);
		printf("Case #%d: ",cases);
		if (number == 0 || ret == -1) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << ret << endl;
		}
	}
}