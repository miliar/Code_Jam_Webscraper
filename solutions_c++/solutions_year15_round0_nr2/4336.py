#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <map>
#include <utility>
#include <set>
#include <functional>
#include <algorithm>

using namespace std;

int get_min_minutes(multiset<int, greater<int> > p, int eat_m, int max_minut)
{
	if (eat_m >= max_minut) {
		return *p.begin() + eat_m;
	}
	multiset<int, greater<int> >::iterator it = p.begin();
	int max_day = *it;

	int first, second;
	int local_min = *p.begin() + eat_m;
	eat_m++;
	for (int i = 1; i <= max_day / 2; ++i) {
		first = i;
		second = max_day - first;

		int comp_val;
		if (++it == p.end()) {
			comp_val = max(first, second) + eat_m;
		}
		else {
			comp_val = max(*it + eat_m, max(first, second) + eat_m);
		}
		--it;

		multiset<int, greater<int> > c = p;
		c.erase(c.begin());
		c.insert(first);
		c.insert(second);

		int val;
		if (eat_m < max_minut) {
			val = get_min_minutes(c, eat_m, max_minut);
			local_min = min(local_min, min(val, comp_val));
		}
	}

	return local_min;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	cin >> cases;
	
	for (int test = 1; test <= cases; ++test) {
		int d;
		cin >> d;
		multiset<int, greater<int> > p;
		for (int i = 0; i < d; ++i) {
			int pi;
			cin >> pi;
			p.insert(pi);
		}

		int minut = *p.begin();
		int eat_m = 0;
		
		minut = get_min_minutes(p, eat_m, min(minut, 5));
		/*while (eat_m < minut) {
			multiset<int, greater<int> >::iterator it = p.begin();
			int max_day = *it;

			int min_minut = 100000;
			int first, second;
			for (int i = 1; i < max_day / 2; ++i) {
				first = i;
				second = max_day - first;
			}
			first = max_day / 2;
			second = max_day - first;
			int comp_val;
			if (++it == p.end()) {
				comp_val = max(first, second) + eat_m;
			}
			else {
				comp_val = max(*it + eat_m, max(first, second) + eat_m);
			}
			--it;

			if (comp_val <= minut) {
				minut = comp_val;
			}
			p.erase(it);
			p.insert(first);
			p.insert(second);
			eat_m++;
		}*/

		cout << "Case #" << test << ": " << minut << endl;
	}

	return 0;
}