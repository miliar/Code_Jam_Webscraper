#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
using namespace std;

int matrix[4][4] = {
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};

int mult(int a, int b) {
	if (a<0 && b <0) return matrix[abs(a)-1][abs(b)-1];
	if (a < 0 || b < 0) return 0-matrix[abs(a)-1][abs(b)-1];
	return matrix[a-1][b-1];
}

bool answer(string a) {
	int cumu = 1;
	int firsti = -1;
	int lastk = -1;
	for (int i = 0; i < a.size(); i++) {
		int current = 1;
		if (a[i] != '1') current = a[i]-'g';
		cumu = mult(cumu, current);
		if (cumu == 2 && firsti == -1) firsti = i;
		if (cumu == 4) lastk = i;
	}
	if (cumu != -1) return false;
	if (firsti == -1 || lastk == -1 || firsti > lastk) return false;
	return true;
}

int main()
{
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int l, x;
		cin >> l >> x;
		string inp="", orig;
		cin >> orig;
		for (int i = 0; i < x; i++) {
			inp += orig;
		}
		if (answer(inp)) printf("Case #%d: YES\n", _t);
		else printf("Case #%d: NO\n", _t);
	}
    return 0;
}
