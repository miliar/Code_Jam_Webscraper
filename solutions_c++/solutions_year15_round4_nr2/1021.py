#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
using namespace std;
ifstream in("in.txt");
ofstream out("out.txt");
int t;
int n;
double v,x;
struct sc {
	double r,c,w,t;
};
vector <sc> a;
bool csrt(sc p,sc q) {
	return (p.c<q.c);
}
int main() {
	out.setf(ios::fixed);
	out.precision(6);
	in >> t;
	for (int i=1;i<=t;i++) {
		in >> n >> v >> x;
		a.resize(n);
		for (int j=0;j<n;j++) in >> a[j].r >> a[j].c;
		for (int j=0;j<n;j++) a[j].c -= x;
		sort(a.begin(),a.end(),csrt);
		if (n == 1) {
			if (a[0].c == 0.) {
				out << "Case #" << i << ": " << v/a[0].r << "\n";
			} else {
				out << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
			}
		} else if (n == 2) {
			if (a[0].c <= 0. && a[1].c >= 0.) {
				if (a[0].c == a[1].c) {
					out << "Case #" << i << ": " << v/(a[0].r + a[1].r) << "\n";
				} else {
					a[0].w = v * a[1].c / (a[1].c - a[0].c);
					a[1].w = v * a[0].c / (a[0].c - a[1].c);
					for (int j=0;j<2;j++) a[j].t = a[j].w / a[j].r;
					out << "Case #" << i << ": " << max(a[0].t,a[1].t) << "\n";
				}
			} else {
				out << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
			}
		} else {
			if (a[0].c <= 0. && a[n-1].c >= 0.) {
				out << "Case #" << i << ": " << 0. << "\n";
			} else {
				out << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
			}
		}
	}
	return 0;
}
