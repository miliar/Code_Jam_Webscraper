#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
using namespace std;

double c, f, x;
double basicF = 2.0, currentF;
double i, j;
void go() {
	cin >> c; cin >> f; cin >> x;
	currentF = basicF;
	i = x / currentF;
	j = c / currentF + x / (currentF + f);
	while(true){
		if(i > j){
			currentF += f;
			i = j;
			j = j - (x / currentF) + (c / currentF) + (x / (currentF + f));
			}else {
			break;
		}
	}
	cout << i;
}

int main() { freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
cout << fixed << setprecision(6);

int testn;
cin >> testn;
for (int testc = 1; testc <= testn; testc++) {
	cout << "Case #" << testc << ": ";
	go();
	cout << '\n';
}
int i = 0;
}
