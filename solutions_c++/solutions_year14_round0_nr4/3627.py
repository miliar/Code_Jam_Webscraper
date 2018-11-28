#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

list<double> read_blocks(unsigned n)
{
	list<double> ret;
	
	while (n-- > 0) {
		double v;
		
		cin >> v;
		ret.push_back(v);
	}
	
	return ret;
}

int deceitful_war(list<double> a, list<double> b)
{
	int score = 0;
	
	while (!a.empty()) {
		auto it = upper_bound(a.begin(), a.end(), b.front());
		if (it == a.end()) {
			a.pop_back();
			b.pop_back();
		}
		else {
			a.erase(it);
			b.pop_front();
			++score;
		}
	}
	
	return score;
}

int truthful_war(list<double> a, list<double> b)
{
	int score = 0;
	
	while (!a.empty()) {
		auto it = upper_bound(b.begin(), b.end(), a.front());
		if (it == b.end()) {
			b.pop_front();
			++score;
		}
		else {
			b.erase(it);
		}
		a.pop_front();
	}
	
	return score;
}

int main()
{
	using namespace std;
	
	unsigned n_cases;
	cin >> n_cases;
	
	for (int case_no=1; case_no<=n_cases; ++case_no) {
		list<double> a, b;
		unsigned n;
		
		cin >> n;
		a = read_blocks(n);
		b = read_blocks(n);
		
		a.sort();
		b.sort();
		
		cout << "Case #" << case_no << ": " << deceitful_war(a, b) << ' ' << truthful_war(a, b) << endl;
	}
	return 0;
}

