#include <set>
#include <iostream>
using namespace std;

int main(void)
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ti++) {
		int n, x;
		cin >> n >> x;
		multiset<int> v;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			v.insert(a);
		}
		int ret = 0;
		while (!v.empty()) {
			auto it = --v.end();
			int a = *it;
//cerr << a << " ";
			v.erase(it);
			if (!v.empty()) {
				auto it2 = v.upper_bound(x - a);
				if (it2 != v.begin()) {
					--it2;
					int b = *it2;
//	cerr << b << " ";
					v.erase(it2);
				}
			}
//	cerr << endl;
			ret++;
		}
		cout << "Case #" << ti << ": " << ret << endl << flush;
	}
	return 0;
}
