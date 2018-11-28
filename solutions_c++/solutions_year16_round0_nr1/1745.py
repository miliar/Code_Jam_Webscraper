#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <set>
#include <string>
#include <iomanip>
 
using namespace std;
 
int main()
{

	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {

		int N;

		cin >> N;

		if (N == 0) {
      	cout << "Case #" << i+1 << ": ";
			cout << "INSOMNIA" << endl;
			continue;
		}

		set<int> s;
		for (int j = 1; true; j++) {

			int k = N * j;

			while (k >= 10) {
				s.insert(k%10);
				k = k/10;
			}

			s.insert(k);

			if (s.size() == 10) {
      		cout << "Case #" << i+1 << ": ";
				cout << N * j << endl;
				break;
			}
		}
	}

	return 0;
}
