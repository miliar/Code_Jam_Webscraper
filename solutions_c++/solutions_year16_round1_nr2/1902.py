#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

vector <int> vec;

int main()
{
	int t, n, var;
	int i, j, k;
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	cin >> t;
	for (i = 0; i < t; i++) {
		cin >> n;
		k = (2*n*n - n);
		vec.clear();
		for (j = 0; j < k; j++) {
			cin >> var;
			//cout << "VAR: " << var << endl;
			if (find(vec.begin(), vec.end(), var) == vec.end()) {
				//cout << "Insert" << endl;
				vec.push_back(var);
			} else {
				//cout << "Erase" << endl;
				vec.erase(remove(vec.begin(), vec.end(), var), vec.end());
			}
		}
		sort(vec.begin(), vec.end());
		cout << "Case #" << i + 1 << ":";
		vector<int>::iterator v = vec.begin();
		while( v != vec.end()) {
			cout << " " << *v;
			v++;
		}
		cout << endl;	
	}	
	return 0;
}
