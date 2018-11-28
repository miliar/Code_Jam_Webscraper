#include <iostream>
#include <set>
#include <map>
using namespace std;

map<multiset<int>, int> best;

int bestTime(multiset<int> &cakes)
{
	if (best.find(cakes) != best.end()) return best[cakes];
	int b = *(cakes.rbegin());
	int be = b;
	if (b > 3)
	{
		multiset<int> cakes2 = cakes;
		cakes2.erase(--cakes2.end());
		for (int i = 2; i <= b/2; ++i)
		{
			multiset<int>::iterator j = cakes2.insert(i);
			multiset<int>::iterator k = cakes2.insert(b-i);
			int c = 1 + bestTime(cakes2);
			if (c < be) be = c;
			cakes2.erase(k); cakes2.erase(j); 
		}
	}
	best[cakes] = be;
	return be;
}

int main()
{
	int T; cin >> T;
	for (int trials = 1; trials <= T; ++trials)
	{
		int D; cin >> D;
		multiset<int> cakes;
		for (int i = 0; i < D; ++i)
		{
			int c; cin >> c;
			cakes.insert(c);
		}
		cout << "Case #" << trials << ": " << bestTime(cakes) << endl;
	}
}
