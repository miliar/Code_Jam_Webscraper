#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int  k = 1; k <= t; ++k) {
		ll n;
		vector<bool> mark(10, false);
		int num = 10;
		cin >> n;
		int lastIndex = -1;
		for (int i = 1; i <= 10000000 && lastIndex == -1; ++i) {
			ll curN = n * i;
			while (curN != 0) {
				int dig = curN % 10;	
				if (mark[dig] == false) {
					mark[dig] = true;
					--num;
					if (num == 0) {
						lastIndex = i;
						break;
					}
				}
				curN /= 10;
			}
		}
		cout << "Case #" << k << ": ";
		if (num == 0) {
			cout <<  static_cast<ll>(lastIndex) * n << endl;
		} else {
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}