#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		int n;
		cin >> n;
		vector<float> a(n), b(n);
		for (int i = 0; i < n; i++) 
			cin >> a[i];
		for (int i = 0; i < n; i++) 
			cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int optimal = 0, j = 0;
		for (int i = 0; i < n; i++) {
			for (; j < n; j++)
				if (a[i] <= b[j]) {
					optimal++;
					j++;
					break;
				}
		}
		optimal = n - optimal;
		int non_optimal = 0;
		int lp = 0, rp = n - 1;
		for (int i = 0; i < n; i++) {
			if (a[i] > b[lp]) {
				non_optimal++;
				lp++;
			} else {
				rp--;
			}
		}
		cout << "Case #" << k << ": ";
		cout << non_optimal << " " << optimal << endl;
	}
}
