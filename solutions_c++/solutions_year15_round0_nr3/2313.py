#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>

#pragma comment(linker, "/STACK:133217728")

using namespace std;

int x[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};

int f(int a, int b) {
	int sign = 1;
	if(a < 0) sign *= -1, a *= -1;
	if(b < 0) sign *= -1, b *= -1;

	return x[a][b] * sign;
}

int ff(char ch) {
	if(ch == 'i') return 2;
	if(ch == 'j') return 3;
	return 4;
}
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);

    int T;
	cin >> T;
	int cnt = 0;
	for(int t=1; t<=T; t++) {
		vector <int> x, z;
		int n, k;
		cin >> n >> k;
		string s = "", ss;
		cin >> ss;
		for(int i=0; i<k; i++)
			s += ss;
		int cur = 1;
		for(int i=0; i<s.length(); i++) {
			cur = f(cur, ff(s[i]));

			if(cur == 2)
				x.push_back(i);
		}

		cur = 1;
		for(int i=s.length()-1; i>0; i--) {
			cur = f(ff(s[i]), cur);
			if(cur == 4)
				z.push_back(i);
		}

		bool ok = 0;

		for(int i=0; i<x.size() && !ok; i++)
			for(int j=0; j<z.size() && !ok; j++)
				if(x[i] < z[j]) {
					int cur = 1;
					for(int k=x[i]+1; k<z[j]; k++)
						cur = f(cur, ff(s[k]));
					//if(x[i] == 2 && z[i] == 6) cout << "###" << cur << endl;
					if(cur == 3) ok = 1;

				}
				
		//cout << "x: " ; for(int i=0; i<x.size(); i++) cout << x[i] << " "; cout << endl;
		//cout << "z: " ; for(int i=0; i<z.size(); i++) cout << z[i] << " "; cout << endl;
		cout << "Case #" << t << ": ";
		if(ok)  cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
    return 0;
}