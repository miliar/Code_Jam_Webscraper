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
	int t,n,p,r,s;
	in >> t;
	int nn(12);
	vector <int> pp(nn),rr(nn),ss(nn);
	vector <string> tt1(nn,""),tt2(nn,""),tt3(nn,"");
	pp[0] = 1;
	rr[0] = 1;
	ss[0] = 0;
	tt1[0] = "PR";
	tt2[0] = "RS";
	tt3[0] = "PS";
	for (int i=1;i<nn;i++) {
		pp[i] = pp[i-1] + ss[i-1];
		rr[i] = rr[i-1] + pp[i-1];
		ss[i] = ss[i-1] + rr[i-1];
		tt1[i] = min(tt1[i-1],tt2[i-1])+max(tt1[i-1],tt2[i-1]);
		tt2[i] = min(tt2[i-1],tt3[i-1])+max(tt2[i-1],tt3[i-1]);
		tt3[i] = min(tt3[i-1],tt1[i-1])+max(tt3[i-1],tt1[i-1]);
	}
	for(int i=1;i<=t;i++) {
		in >> n >> r >> p >> s;
		n--;
		if (pp[n] == p && rr[n] == r && ss[n] == s) {
			out << "Case #" << i << ": " << tt1[n] << "\n";
		} else if (pp[n] == r && rr[n] == s && ss[n] == p) {
			out << "Case #" << i << ": " << tt2[n] << "\n";
		} else if (pp[n] == s && rr[n] == p && ss[n] == r) {
			out << "Case #" << i << ": " << tt3[n] << "\n";
		} else {
			out << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
		}
	}
	return 0;
}
