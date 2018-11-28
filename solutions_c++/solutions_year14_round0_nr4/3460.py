#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <windows.h>
#include <string>
#include <cctype>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <initializer_list>
#include <exception>
#include <time.h>

typedef long long ll;

using namespace std;

int war(vector <double> n, vector <double> k) {
	int res = 0;
	while (n.size() > 0) {
		bool flag = false;
		for (int i = 0; i < k.size(); ++i) {
			if (n[0] < k[i]) {
				flag = true;
				k.erase(k.begin() + i);
				break;
			}
		}
		if (!flag) {
			++res;
		}
		n.erase(n.begin());
	}
	return res;
}

int deceifulWar(vector <double> n, vector <double> k) {
	int res = 0;
	while (n.size() > 0) {
		if (n[n.size() - 1] > k[k.size() - 1]) {
			++res;
			n.pop_back();
			k.pop_back();
		}
		else {
			n.erase(n.begin());
			k.pop_back();
		}
	}
	return res;
}

#define ONLINE_JUDGE
int main(int argc, char **argv) {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		int n = 0;
		cin >> n;
		vector <double> naomi(n, 0), ken(n, 0);
		for (int i = 0; i < n; ++i) {
			cin >> naomi[i];
		}
		for (int i = 0; i < n; ++i) {
			cin >> ken[i];
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		cout << deceifulWar(naomi, ken) << ' ' << war(naomi, ken) << endl;
	}

	//system("pause");
	return 0;
}
