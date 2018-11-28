using namespace std;

#define MAX_MOTES 201
#include <iostream>
#include <cmath>

int a, n, added, removed;
int motes[MAX_MOTES];

int compareInt(const void * a, const void * b) {
	return *(int *)a - *(int *)b;
}

int farthest() {
	int total = a;
	for (int i = 0; i < n + added; i++) {
		if (total > motes[i]) {
			total += motes[i];
		} else {
			return total;
		}
	}
	return total;
}

int addMote() {
	if (added < n) {
		int mote_val = farthest() - 1;
		if (mote_val == 0) {
			return -1;
		}
		motes[n + added] = mote_val;
		added++;
		qsort(motes, n + added, sizeof(int), compareInt);
		return mote_val;
	} else {
		return 0;
	}
}

int removeMote() {
	if (removed < n) {
		removed++;
		return 1;
	} else {
		return 0;
	}
}

int atest() {
	//cout << "added " << added << " removed " << removed << endl;
	//cout << "far " << farthest() << " target " << motes[n + added - removed - 1] << endl;
	if (farthest() > motes[n + added - removed - 1]) {
		return 0;
	}
	int min = n;
	int is_remove;
	if (is_remove = removeMote()) {
		min = atest() + 1;
		removed--;
	} else {
		min = 0;
	}
	int add_val = addMote();
	if (add_val > 0) {
		int min2 = atest() + 1;
		if (min2 < min) {
			min = min2;
		}
		for (int i = 0; i < n + added; i++) {
			if (motes[i] == add_val) {
				motes[i] = 9999999;
				qsort(motes, n + added, sizeof(int), compareInt);
				added--;
				break;
			}
		}
	} else if (add_val == 0) {
		min = 0;
	}
	return min;
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test < tests + 1; test++) {
		cin >> a;
		cin >> n;
		added = 0;
		removed = 0;
		for (int i = 0; i < n; i++) {
			cin >> motes[i];
		}
		qsort(motes, n, sizeof(int), compareInt);
		cout << "Case #" << test << ": " << atest() << endl;
	}
	return 0;
}