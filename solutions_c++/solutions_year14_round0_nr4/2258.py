#include <vector>
#include <iostream>
#include <functional>
#include <algorithm>
#include <set>

#pragma warning(disable : 4996)

using namespace std;

int deceitful_war(vector<double> &a, vector<double> &b)
{
	//sort(b.begin(), b.end(), greater<double>());
	set<double> c; int n = a.size();
	for (int i = 0; i < n; i++)
		c.insert(a[i]);
	int s = 0;
	for (int i = 0; i < n; i++) {
		set<double>::iterator it = c.lower_bound(b[i]);
		if (it != c.end()) {
			c.erase(it);
			s++;
		}
		else
			c.erase(c.begin());
	}
	return s;
}

int war(vector<double> &a, vector<double> &b)
{
	set<double> c;
	int n = b.size();
	for (int i = 0; i < n; i++)
		c.insert(b[i]);
	int s = 0;
	for (int i = 0; i < n; i++) {
		set<double>::iterator it = c.lower_bound(a[i]);
		if (it == c.end()) {
			s++;
			c.erase(c.begin());
		}
		else
			c.erase(it);
	}
	return s;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		vector<double>a(n), b(n);
		for (int j = 0; j < n; j++)
			cin >> a[j];
		for (int j = 0; j < n; j++)
			cin >> b[j];
		cout << "Case #" << i + 1 << ": " << deceitful_war(a, b) << " " << war(a, b) << endl;
	}
	return 0;
}