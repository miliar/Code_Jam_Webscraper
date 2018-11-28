#include<iostream>
#include<map>

using namespace std;

map<long long, long long> mymap;

void decompose(long long  n, bool (&collection)[10]) {
	// cout << n << endl;
	while (n) {
		collection[n%10] = true;
		n = n / 10;
	}
}

int validate(bool (&collection)[10]) {
	int res = 0;
	for (int i = 0; i < 10; i++) {
		res += collection[i];
	}
	return res;
}

int calcStep(long long n) {
	long long step = n;
	bool collection [10] = {false};
	decompose(step, collection);
	while (validate(collection) < 10) {
		step += n;
		decompose(step, collection);
	}
	mymap[n] = step;
	return step;
}

int main () {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		long long n; cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			map<long long, long long>::iterator it = mymap.find(n);
			int res;
			if (it != mymap.end()) {
				res = it->second;
			}
			else {
				res = calcStep(n);
			}
			cout << "Case #" << i << ": " << res << endl;
		}
	}
}
