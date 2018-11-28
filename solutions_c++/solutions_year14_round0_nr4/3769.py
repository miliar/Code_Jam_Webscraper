#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
#include <iostream>
#include <iomanip>

using namespace std;

#define INF (1<<29)
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)

double a1[1005], a2[1005];
int n;

// Deceitful war
int strategy1() {
	set<double> A1;
	for(int i = 0; i < n; ++i)
		A1.insert(a1[i]);
	sort(a2, a2+n);
	
	int points = 0;
	int b = 0, e = n - 1;
	while(b <= e) {
		set<double>::iterator it1 = A1.begin(), it2 = A1.end(), it;
		--it2;
		
		if(*it2 > a2[e]) {
			it = A1.upper_bound(a2[b]);
			++b;
			A1.erase(it);
			++points;
		}
		else {
			--e;
			A1.erase(it1);
		}
	}
	
	return points;
}

// War
int strategy2() {
	sort(a1, a1 + n);
	set<double> A2;
	for(int i = 0; i < n; ++i)
		A2.insert(a2[i]);
	
	int points = 0;
	int b = 0, e = n - 1;
	while(b <= e) {
		set<double>::iterator it1 = A2.begin(), it2 = A2.end(), it;
		--it2;
		
		if(a1[e] > *it2) {
			--e;
			A2.erase(it1);
			++points;
		}
		else {
			it = A2.upper_bound(a1[e]);
			--e;
			A2.erase(*it);
		}
	}
	
	return points;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cin >> n;
		for(int i = 0; i < n; ++i)
			cin >> a1[i];
		for(int i = 0; i < n; ++i)
			cin >> a2[i];
		cout << "Case #" << t << ": ";
		cout << strategy1() << " " << strategy2() << endl;
	}
		
	return 0;
}
