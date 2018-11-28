///https://code.google.com/codejam/contest/2974486/dashboard#s=p0

#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

// forward declaration
void Problem1();
void Problem2();

int main(){
	Problem2();
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

void Problem2(){
	int t;
	cin >> t;
	int max = t;
	while (t--){
		double c, f, x;
		cin >> c >> f >> x;
		double n = ((x - c)*(2 + f) - (2 * x)) / (c * f);
		if (n <= 0){
			cout << "Case #" << max - t << ": " << setprecision(13) << x / 2;
		}
		else{
			double intpart;
			if (modf(n, &intpart) != 0.0){
				intpart = intpart + 1;
			}
			double ans = 0;
			for (int i = 0; i < intpart; i++)
			{
				ans = ans + c / (2 + (f * i));
			}
			ans += x / (2 + (f * intpart));
			cout << "Case #" << max - t << ": " << setprecision(13) << ans;
		}
		cout << "\n";
	}
}