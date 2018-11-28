#include <iostream>
#include <limits>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int j = 1; j <= T; ++j) {
		int Smax;
		int standing = 0;
		int extras = 0;
		string counts;
		cin >> Smax >> counts;
		//cout << Smax << ' ' << counts.length() << endl;
		for (int i = 0; i <= Smax; i++) {
			if (standing < i) {
				extras += i - standing;
				standing = i;
			}
			standing += counts[i] - '0';
		}
		cout << "Case #" << j << ": " << extras << endl;
	}
	return 0;
}

