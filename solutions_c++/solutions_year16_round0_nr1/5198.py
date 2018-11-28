#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <set>
#include <vector>


using namespace std;

/*long long f (int n) {
	long long k = 0, m = 0;
	if (n == 0) {
			return -1;
		} 
		else {
			set <int> s;
			int j = 1;
			while (s.size() < 10) {
				k = n * j;
				m = k;
				while (k > 0) {
					s.insert(k % 10);
					k /= 10;
				}
				j++;
			}
			return m;
		}
}*/

int main() {
	/*for (int i = 0; i < 2000001; i++) {
		if ((i % 1000) == 0) {
			cerr << f(i) << endl;
		}
	}*/
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, m = 0, k = 0;
		cin >> n;
		cout << "Case #" << i + 1 << ":" << " ";
		if (n == 0) {
			cout << " INSOMNIA" << endl;
		} 
		else {
			set <int> s;
			int j = 1;
			while (s.size() < 10) {
				k = n * j;
				m = k;
				while (k > 0) {
					s.insert(k % 10);
					k /= 10;
				}
				j++;
			}
			cout << m << endl;
		}

	}
	//rm a.out; g++ A.cpp; ./a.out
}