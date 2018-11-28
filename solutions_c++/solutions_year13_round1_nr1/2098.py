#include <iostream>
#include <fstream>
#include <climits>

using namespace std;

#define PI 3.1415926535897932384626433832795

long long f(long long n) {
	return 2*n*n-n-2;
}

int main() {
	int nTestCases;
	ifstream in("A-small-attempt0.in");
	ofstream out("out");
	in>>nTestCases;
	for(int testcase=0; testcase<nTestCases; testcase++) {
		long long r, t;
		in>>r>>t;
		int n_black_rings=0;
		for(long long r_in=r, r_out=r+1; ;r_in+=2, r_out=r_in+1) {
			long long paint_needed=(r_out*r_out-r_in*r_in);
			if(paint_needed>t)
				break;
			t-=paint_needed;
			n_black_rings++;
		}
		out<<"Case #"<<(testcase+1)<<": "<<n_black_rings<<endl;
	}
}