#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

map<vector<int> , int> o;
vector<int> g;

bool isValid(int idx, int cur_idx, const vector<vector<int> >& lists, vector<vector<int> >& mat, bool dir) {
	if (idx == 0) {
		return true;
	}
	bool okay = 1;
	if (dir) {
		for (int j = 0; j < mat.size(); j++) {
			if (lists[cur_idx][j] <= mat[idx - 1][j]){
				okay = false;
				break;
			}
		}
	} else {
		for (int i = 0; i < mat.size(); i++) {
			if (lists[cur_idx][i] <= mat[i][idx - 1]){
					okay = false;
					break;
				}
			}
	}
	return okay;

}

void fillMat(int idx, int cur_idx, const vector<vector<int> >& lists, vector<vector<int> >& mat, bool dir) {
	if (dir) {
		for (int j = 0; j < mat.size(); j++) {
			mat[idx][j] = lists[cur_idx][j];
		}
	} else {
		for (int i = 0; i < mat.size(); i++) {
			mat[i][idx] = lists[cur_idx][i];
		}
	}
}
bool Gen(int idx, int cur_idx, const vector<vector<int> >& lists, int n, vector<vector<int> >& mat, bool dir) {
	if (idx == n) {

//		for (int i = 0 ; i < n ; i++) {
//			for (int j = 0 ; j < n; j++) {
//				cout << mat[i][j] <<" ";
//			}
//			cout << endl;
//		}
//		cout << endl;

		map<vector<int> , int> s = o;
		if (dir) {
			for (int i = 0; i < n; i++) {
				vector<int> tmp (n);
				int idx = 0;
				for (int j = 0; j < n; j++) {
					tmp[idx++] = mat[i][j];
				}
				s[tmp]--;
			}

//			for (const auto v : s) {
//				for (auto x : v.first) cout << x <<" ";
//				cout << " -> " << v.second<< endl;
//			}
			int miss = 0;
			vector<int> goal;
			for (int j = 0; j < n; j++) {
				if (miss > 1) {
					return false;
				}
				vector<int> tmp (n);
				int idx = 0;
				for (int i = 0; i < n; i++) {
					//cout << mat[i][j] << " ";
					tmp[idx++] = mat[i][j];
				}
				//cout << endl;
				if (s.find(tmp) == s.end()) {
					goal = tmp;
					miss++;
					continue;
				}
				if (s[tmp] == 0) {
					goal = tmp;
					miss++;
					continue;
				}
				s[tmp]--;
			}
			if (miss > 1) {
				return false;
			}
			g = goal;
		} else {
			for (int j = 0; j < n; j++) {
				vector<int> tmp (n);
				int idx = 0;
				for (int i = 0; i < n; i++) {
					tmp[idx++] = mat[i][j];
				}
				s[tmp]--;
			}
			int miss = 0;
			vector<int> goal;
			for (int i = 0; i < n; i++) {
				if (miss > 1) {
					return false;
				}
				vector<int> tmp (n);
				int idx = 0;
				for (int j = 0; j < n; j++) {
					tmp[idx++] = mat[i][j];
				}
				if (s.find(tmp) == s.end()) {
					goal = tmp;
					miss++;
					continue;
				}
				if (s[tmp] == 0) {
					goal = tmp;
					miss++;
					continue;
				}
				s[tmp]--;
			}
			if (miss > 1) {
				return false;
			}
			g = goal;
		}
		return true;
	}
	if (cur_idx == lists.size()) {
		return false;
	}
	if (isValid(idx, cur_idx, lists, mat, dir)) {
		fillMat(idx, cur_idx, lists, mat, dir);
		if (Gen(idx + 1 , cur_idx + 1, lists, n , mat, dir)) {
			return true;
		}
	}
	if (Gen(idx, cur_idx + 1, lists, n , mat, dir)) {
		return true;
	}
	return false;
}
int main() {
	freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
	int t, n;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cin >> n;
		cout << "Case #" << tt <<": ";
		vector<vector<int> > lists;
		vector<int> temp(n);
		o.clear();
		for (int i = 0; i < 2 * n -1; i++) {
			for (int j = 0; j < n; j++) {
				cin >> temp[j];
			}
			lists.push_back(temp);
			o[temp]++;
		}
		vector<vector<int> > mat(n , vector<int>(n));
		sort(lists.begin(), lists.end());
		if (!Gen(0, 0, lists, n, mat, 1)) {
			if (!Gen(0, 0, lists, n, mat, 0)) {
				cout <<"BAD\n";
			}
		}
		for (int i = 0 ; i < n ; i++) {
			cout << g[i];
			if (i + 1 < n) cout <<" ";
		}
		cout << endl;


//				for (int i = 0 ; i < n ; i++) {
//					for (int j = 0 ; j < n; j++) {
//						cout << mat[i][j] <<" ";
//					}
//					cout << endl;
//				}
//				cout << endl;

	}
	return 0;
}
