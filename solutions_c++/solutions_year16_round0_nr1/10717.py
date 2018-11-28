#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
using namespace std;

int main() {
	vector<unsigned long long> ref = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	vector<unsigned long long> mo = {};
	unsigned int T;
	unsigned long long N;
	cin >> T;

	for (int i = 0; i < T; i++)	{
		cin >> N;
		if (N == 0)
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else {
			unsigned long long result = N;
			unsigned long long bk = N;
			while (mo != ref) {
				if (bk != N)
					result += N;
				bk = result;
				while (bk != 0) {
					unsigned long long tmp = bk % 10;
					if (find(mo.begin(), mo.end(), tmp) == mo.end())
						mo.push_back(tmp);
					bk /= 10;
				}
				sort(mo.begin(), mo.end());
			}			
			cout << "Case #" << i + 1 << ": " << result << endl;
			mo.clear();
		}
	}
	return 0;
}