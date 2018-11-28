#include <iostream>
#include <set>


using namespace std;

int main()
{
	int cases = 0, T, N;
	cin >> T;
	while(T--) {
		set<double> naomi, ken;
		double tmp;
		cin >> N;
		int first = 0;
		int second =0;
		int k = N;
		while (k--) {
			cin >> tmp;
			naomi.insert(tmp);
		}
		k = N;
		while (k--) {
			cin >> tmp;
			ken.insert(tmp);
		}
		set<double> n2 = naomi;
		set<double> k2 = ken;
		for (set<double>::iterator i = k2.begin(); i != k2.end(); i++) {
			set<double>::iterator j = n2.lower_bound(*i);
			if ( j != n2.end()) {
				n2.erase(j);
				first++;
			} else {
				n2.erase(n2.begin());
			}
		}

		for (set<double>::iterator i = naomi.begin(); i != naomi.end(); i++) {
			set<double>::iterator j = ken.lower_bound(*i);
			if ( j != ken.end()) {
				ken.erase(j);
			} else {
				ken.erase(ken.begin());
				second++;
			}
		}
		cout << "Case #" << ++cases << ": " << first<< " "<< second << endl;
	}
}