#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;
int T, N, x, y, z;
vector<double> Naomi, Ken;
int main()
{
	cin >> T;
	for (x = 1; x <= T; ++x)
	{
		cin >> N;
		Naomi.clear();
		Ken.clear();
		y = z = 0;
		double mass;
		for (int i = 0; i < N; ++i)
		{
			cin >> mass;
			Naomi.push_back(mass);
		}
		sort(Naomi.begin(), Naomi.end());
		for (int i = 0; i < N; ++i)
		{
			cin >> mass;
			Ken.push_back(mass);
		}
		sort(Ken.begin(), Ken.end());
		vector<double>::iterator itN = Naomi.begin();
		vector<double>::reverse_iterator ritN = Naomi.rbegin();
		vector<double>::reverse_iterator ritK = Ken.rbegin();
		vector<double>::iterator itK = Ken.begin();
		// while(*itN < *itK && itN != Naomi.end()) {
		// 	++itN; ++ritK;
		// }
		// y = Naomi.end() - itN;

		while (itN != Naomi.end()) {
			while (*itN < *itK && itN != Naomi.end()) {
				++itN;
				++ritK;
				++y;
			}
			if (itK + y == Ken.end()) break;
			++itK;
			++itN;
		}
		y = N - y;

		itN = Naomi.begin();
		itK = Ken.begin();
		while (itN != Naomi.end()) {
			while (*itK < *itN && itK != Ken.end()) {
				++z;
				++itK;
			}
			if (itK == Ken.end()) break;
			++itK;
			++itN;
		}

		cout << "Case #" << x << ": " << y << " " << z << endl;
	}
}