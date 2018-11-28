#include <fstream>
#include <cassert>
using namespace std;

int getAns1(const int a[], const int n) {
	int ret = 0;
	for (int i=0; i<n-1; i++) {
		if (a[i+1] < a[i]) 
			ret += a[i] - a[i+1];
	}
	return ret;
}

int getAns2(const int a[], const int n) {
	int ret = 0;
	int del = 0;
	for (int i=0; i<n-1; i++) {
		if (a[i+1] < a[i])
			del = max(del, a[i]-a[i+1]);
	}
	for (int i=0; i<n-1; i++) {
		if (a[i] >= del) ret += del;
		else ret += a[i];
	}
	return ret;
}

int main() {
	int test;
	ifstream fin("A-large.in");
	ofstream fout("pa-large.out");
	assert(fin && fout);
	fin >> test;
	for (int count=1; count<=test; count++) {
		int n;
		fin >> n;
		int a[n];
		for (int i=0; i<n; i++) {
			fin >> a[i];
		}
		fout << "Case #" << count << ": " << getAns1(a, n) << " " << getAns2(a, n) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}