#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

struct Party {
	char name;
	int members;
};

int cmpParty(const void* p1, const void* p2) {
	return ((Party*)p2)->members - ((Party*)p1)->members;
}

void sortParties(Party* p, int n) {
	qsort(p, n, sizeof(Party), cmpParty);
}

void evac(Party* p) {
	cout << p->name;
	p->members--;
}

int main() {
	int T, n;
	Party p[26];
	int count;

	cin >> T;

	for(int t=0; t<T; t++) {
		cin >> n;
		count = 0;
		for(int i=0; i<n; i++) {
			p[i].name = 'A' + i;
			cin >> p[i].members;
			count += p[i].members;
		}

		/*for(int i=0; i<n; i++) {
			cout << p[i].name << "(" << p[i].members << ")" << endl;
		}*/

		cout << "Case #" << (t+1) << ": ";

		sortParties(p, n);

		while(p[0].members > 0) {
			evac(p);
			count--;

			if(p[1].members > 0) {
				if(p[1].members != 1 || p[2].members != 1) {
					evac(p+1);
					count--;
				}
			} else if(p[0].members > 0) {
				evac(p);
				count--;
			}
			cout << " ";

			sortParties(p, n);

			/*cout << "[" << count << "] ";
			for(int i=0; i<n; i++) {
				cout << ((p[i].members > count / 2) ? "*" : "") << p[i].name << "(" << p[i].members << ") ";
			}*/
		}

		cout << endl;
	}

	return 0;
}
