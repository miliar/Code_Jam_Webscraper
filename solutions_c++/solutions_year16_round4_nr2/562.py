#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <iterator>
#include <deque>
using namespace std;
const long long int modl=1000000007;
ifstream in("in.txt");
ofstream out("out.txt");
int main() {
	out.setf(ios::fixed);
	out.precision(7);
	int t,n,k;
	in >> t;
	vector <double> p,q;
	for(int i=1;i<=t;i++) {
		in >> n >> k;
		p.resize(n);
		for (int j=0;j<n;j++) {
			in >> p[j];
		}
		sort(p.begin(),p.end());
		double qmax(0.);
		for (int j=0;j<=k;j++) {
			q.assign(k+1,0.);
			q[0] = 1.;
			for (int l=0;l<j;l++) {
				for (int m=k;m>=1;m--) {
					q[m] = q[m] * (1.-p[l]) + q[m-1] * p[l];
				}
				q[0] = q[0] * (1.-p[l]);
			}
			for (int l=n-k+j;l<n;l++) {
				for (int m=k;m>=1;m--) {
					q[m] = q[m] * (1.-p[l]) + q[m-1] * p[l];
				}
				q[0] = q[0] * (1.-p[l]);
			}
			qmax = max(qmax, q[k/2]);
			
		}
		out << "Case #" << i << ": " << qmax << "\n";
	}
	return 0;
}
