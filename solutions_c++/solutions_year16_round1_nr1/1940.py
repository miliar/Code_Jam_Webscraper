#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
using namespace std;

int main()
{
	int t;
	int i, j, k;
	string s, sp;
	string first = ";";
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	cin >> t;
	for (i = 0; i < t; i++) {
		sp.clear();
		s.clear();
		cin >> s;
		//cout << s << endl;
		k = s.size();
		for (j = 0; j < k; j++) {
			//cout << " s[j] : " << s[j] << "   sp[0] : " << sp[0] << endl;
			if (s[j] >= sp[0]) {
				sp = s[j] + sp;
			} else {
				sp = sp + s[j];
			}
		}
		cout << "Case #" << i + 1 << ": "<< sp << endl;
	}	
	return 0;
}
