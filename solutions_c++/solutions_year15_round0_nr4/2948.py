#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <string>

using std::vector;
using std::cin;
using std::cout;
using std::string;
using std::getline;
using std::min;

vector<int> prefix_function (string s) {
	int n = (int) s.length();
	vector<int> pi (n);
	for (int i=1; i<n; ++i) {
		int j = pi[i-1];
		while (j > 0 && s[i] != s[j])
			j = pi[j-1];
		if (s[i] == s[j])  ++j;
		pi[i] = j;
	}
	return pi;
}

vector<int> z_function (string s) {
	int n = (int) s.length();
	vector<int> z (n);
	for (int i=1, l=0, r=0; i<n; ++i) {
		if (i <= r)
			z[i] = min (r-i+1, z[i-l]);
		while (i+z[i] < n && s[z[i]] == s[i+z[i]])
			++z[i];
		if (i+z[i]-1 > r)
			l = i,  r = i+z[i]-1;
	}
	z[0] = s.length();
	return z;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    string str;
    getline(cin, str);
    vector <int> res = z_function(str);
    for (int ind = 0; ind < res.size(); ++ind) {
        cout << res[ind] <<" ";
    }


    return 0;
}
