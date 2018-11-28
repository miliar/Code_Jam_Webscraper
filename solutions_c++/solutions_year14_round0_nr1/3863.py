///https://code.google.com/codejam/contest/2974486/dashboard#s=p0

#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

// forward declaration
void Problem1();

int main(){
	Problem1();
	return 0;
}

void Problem1(){
	int t;
	cin >> t;
	int max = t;
	while (t--){
		short a[16], b[16];
		int ans1, ans2;
		cin >> ans1;
		for (int i = 0; i < 16; i++)
		{
			cin >> a[i];
		}
		int start1 = 4 * (ans1 - 1);
		sort((a + start1), a + start1 + 4);
		cin >> ans2;
		for (int i = 0; i < 16; i++)
		{
			cin >> b[i];
		}
		int start2 = 4 * (ans2 - 1);
		sort(b + start2, b + start2 + 4);

		vector<int> v(4);
		vector<int>::iterator it;
		it = set_intersection((a + start1), a + start1 + 4, b + start2, b + start2 + 4, v.begin());
		v.resize(it - v.begin());
		switch (v.size())
		{
		case 1:
			cout << "Case #";
			cout << max - t;
			cout << ": ";
			cout << v.front();
			break;
		case 0:
			cout << "Case #";
			cout << max - t;
			cout << ": Volunteer cheated!";
			break;
		default:
			cout << "Case #";
			cout << max - t;
			cout << ": Bad magician!";
		}
		cout << "\n";
	}
}