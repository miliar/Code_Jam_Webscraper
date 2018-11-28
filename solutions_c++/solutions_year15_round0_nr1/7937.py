#include <iostream>
using namespace std;

int main()
{

	int t;
	int n;
	char c;
	int count;
	int ans;
	char a[1005];
	int x;

	cin >> t;

	for (int cases = 1; cases <= t; cases++) {
		cin >> n;
		for (int i = 0; i <= n; i++) {
			cin >> a[i];
		}

		x = a[0] - '0';
		count = x;;
		ans = 0;

		for (int i = 1; i <= n; i++) {
			x = a[i] - '0';
			if(x != 0) {
				if(count >= i) {
					count += x;
				}

				else {
					ans += i - count;
					count += x + (i - count);
				}

			}

		}


		cout << "Case #"<<cases<< ": " << ans << "\n";
	}


}





