#include <iostream>
#include <set>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define forn(i, n) for(int i=0; i<(int)(n); i++)

int main()
{
	int nums[] = {1, 4, 9, 121, 484};
	set<int> ps (nums, nums + 7);
	set<int>::iterator itlow, itup;

	int T;
	cin >> T;

	forn(i, T) {
		int A;
		cin >> A;
		int B;
		cin >> B;

		itlow = ps.lower_bound (A);
		itup = ps.upper_bound (B);
		set <int> result (itlow, itup);
		cout << "Case #" << i + 1 << ": " << result.size() << endl;
	}

	return 0;
}
