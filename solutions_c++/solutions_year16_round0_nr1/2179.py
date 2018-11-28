#include <iostream>
#include <vector>

using namespace std;


int main()
{
	int t;
	cin >> t;

	int c = 1;

	while (t--) {
		
		cout << "Case #" << c << ": ";
		c++;

		long long n;
		cin >> n;

		vector<bool> seen(10, false);

		if (n == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			int m = 1;
			bool done = false;
			while (!done) {

				long long test = m * n;
				while (test != 0) {
					seen[test % 10] = true;
					test /= 10;
				}

				done = seen[0] && seen[1] && seen[2] && seen[3] && seen[4] && seen[5] && seen[6] && seen[7] && seen[8] && seen[9]; 
				m++;
			}

			m--;
			cout << m * n << endl;
		}


	}
	return 0;
}

