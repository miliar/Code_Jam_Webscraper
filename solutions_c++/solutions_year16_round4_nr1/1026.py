#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

bool check(vector <int> a) {
	vector <int> temp;
	while (!(a.size() == 1)) {
		temp.clear();
		for (int i = 0; i < a.size(); i += 2) { 
			if (a[i] == a[i+1])
				return false;
			int mn = min(a[i], a[i+1]);
			int mx = max(a[i], a[i+1]);
			if (mn == 1 && mx == 2)
				temp.push_back(1);
			else if (mn == 2 && mx == 3)
				temp.push_back(2);
			else
				temp.push_back(3);
		}
		a = temp;
	}
	return true;
}

int count_ones(int a) {
	int count = 0;
	while (a) {
		++count;
		a &= (a-1);
	}
	return count;
}

pair <int, int> get_ans (int a) {
	if (a == 1)
		return make_pair (1, 2);
	else if (a == 2)
		return make_pair (2, 3);
	else
		return make_pair (1, 3);
}

vector <int> get_moves(int a, int n) {
	vector <int> cur(1, a);
	for (int j = 0; j < n; ++j) {
		vector <int> ncur (2 * cur.size());
		for (int k = 0; k < cur.size(); ++k) {
			pair <int, int> ans = get_ans(cur[k]);
			ncur [k * 2] = ans.first;
			ncur [k * 2 + 1] = ans.second;
		}
		cur = ncur;
	}
	return cur;
}

bool my_less(vector <int> &a, int l1, int l2, int k) {
	for (int i = 0; i < k; ++i)
		if (a[l2+i] < a[l1+i])
			return true;
	return false;
}

void my_sort(vector <int>& a) {
	for (int i = 2; i <= a.size(); i *= 2) {
		for (int j = 0; j < a.size(); j += i)
			if (my_less(a, j, j + i/2, i/2))
				for (int k = 0; k < i/2; ++k)
					swap(a[j+k], a[j+k+i/2]);
	}
}

bool check_moves(vector <int> &a, int r, int p, int s) {
	for (int i = 0; i < a.size(); ++i)
		if (a [i] == 1)
			--p;
		else if (a [i] == 2)
			--r;
		else
			--s;
	if (p != 0 || r != 0 || s != 0)
		return false;
	else
		return true;
}

bool my_less2 (vector <int> &a, vector <int> &b) {
	for (int i = 0; i < a.size(); ++i)
		if (a[i] < b[i])
			return true;
	return false;
}

int main () {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		int n, p, r, s;
		cin >> n >> r >> p >> s;

		vector <int> sol1 = get_moves(1, n);
		vector <int> sol2 = get_moves(2, n);
		vector <int> sol3 = get_moves(3, n);

		bool c1 = check_moves(sol1, r, p, s);
		bool c2 = check_moves(sol2, r, p, s);
		bool c3 = check_moves(sol3, r, p, s);
		if (!c1 && !c2 && !c3) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (c1)
			my_sort(sol1);
		if (c2)
			my_sort(sol2);
		if (c3)
			my_sort(sol3);

		if (!c1)
			if (!c2)
				sol1 = sol3;
			else
				sol1 = sol2;

		if (c2 && my_less2(sol2, sol1))
			swap(sol2, sol1);
		if (c3 && my_less2(sol3, sol1))
			swap(sol3, sol1);

		for (int j = 0; j < sol1.size(); ++j) {
			if (sol1[j] == 1)
				cout << "P";
			else if (sol1[j] == 2)
				cout << "R";
			else
				cout << "S";
		}
		cout << endl;
	}
}