#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
	ifstream in("D-large.in");
	ofstream out("Output.txt");
	int T;
	in >> T;
	for (int n=0; n<T; ++n) {
		int N;
		in >> N;
		float *a1 = new float[N];
		for (int i=0; i<N; ++i) in >> a1[i];
		float *a2 = new float[N];
		for (int i=0; i<N; ++i) in >> a2[i];
		sort(a1, a1+N);
		sort(a2, a2+N);
		int res1 = 0, res2 = 0;
		for (int i=0, j=0; i<N; ++i, ++j) {
			if (a1[i] > a2[j]) ++res1;
			else --j;
		}
		for (int i=0, j=0; i<N && j<N; ++i, ++j) {
			while (j<N && a2[j]<a1[i]) ++j;
			if (j == N) break;
			else ++res2;
		}
		res2 = N - res2;
		out<<"Case #"<<n+1<<": "<<res1<<" "<<res2<<endl;
	}
	return 0;
}