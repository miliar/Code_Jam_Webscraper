#include <iostream>
#include <vector>

using namespace std;

bool canSleep(vector<bool> record) {
	for (vector<bool>::iterator it = record.begin(); it != record.end(); ++it) {
		if ((*it) == false) return false;
	}
	return true;
}

void updateRecord(int num, vector<bool> &v) {
	do {
		int a = num % 10;
		v[a] = true;
		num /= 10;
	} while (num > 0);
}

int countingSheep(int n) {
	if (n == 0) return -1;

	int count = 0;
	int num = 0;
	vector<bool> record(10, false);
	while (!canSleep(record)) {
		++count;
		num = count * n;
		// cout << num << " ";
		updateRecord(num, record);
	}
	return num;
}

int main( int argc, char** argv ) {
	int count = 0;
	cin >> count;
	countingSheep(count);
	for (int i = 0; i < count; ++i) {
		int N;
		cin >> N;
		int num = countingSheep(N);
		cout << "Case #" << i + 1 << ": ";
		if (num == -1) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << countingSheep(N) << endl;
		}
	}
	return 0;
}
