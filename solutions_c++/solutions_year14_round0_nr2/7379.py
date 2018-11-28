#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
using namespace std;
//typedef long long tint;

int main () {
	double c, f, x, h, r;
	int i, t;
	cin >> t;
	for(i = 1; i <= t; i++){
		cin >> c >> f >> x;
		r = 2;
		for(h = 0;((x/r) > ((x/(r+f)) + (c/r)));){
			h += c/r; 
			r+=f;
		}
		h += x/r;
		printf("Case #%d: %.7lf\n", i, h);
	}
	return 0;
}