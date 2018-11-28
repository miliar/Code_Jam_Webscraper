#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
typedef long long LL;
main() {
	FILE *fout = freopen("Dlarge.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		int w = 0;
		int dw = 0;
		set<double> a;
		set<double> acpy;
		set<double> b;
		set<double> bcpy;
		for(int i = 0; i < n; i++){
			double c;
			cin >> c;
			a.insert(c);
			acpy.insert(c);
		}
		for(int i = 0; i < n; i++){
			double c;
			cin >> c;
			b.insert(c);
			bcpy.insert(c);
		}
		for(int i = 0; i < n; i++){
			double beg = *(--b.end());
			double end = *(--a.end());
			if(beg < end){
				b.erase(--b.end());
				a.erase(--a.end());
			} else {
				b.erase(--b.end());
				a.erase(a.begin());
				dw++;
			}
		}
		cout <<  n-dw << " ";
		for(int i = 0; i < n; i++){
			double beg = *(--acpy.end());
		double end = *(--bcpy.end());
			if(beg < end){
				acpy.erase(--acpy.end());
				bcpy.erase(--bcpy.end());
			} else {
				acpy.erase(--acpy.end());
				bcpy.erase(bcpy.begin());
				w++;
			}
		}
		cout << w << endl;
	}
	exit(0);
}