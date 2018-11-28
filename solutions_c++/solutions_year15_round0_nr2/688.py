#include <fstream>
#include <algorithm>
#include <cassert>
using namespace std;

int getAns(int p[], int D) {
	int maxp = *max_element(p, p+D);
	int ans = maxp;
	for (int height = maxp-1; height>=1; height--) {
		int times = 0;
		for (int i=0; i<D; i++) {
			if (p[i]>height) {
				times += (p[i] + height -1) / height - 1;
			}
		}
		if (times + height < ans) 
			ans = times + height;
	}
	return ans;
}

int main() {
	ifstream fin("B-large.in");
	ofstream fout("pb_large.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int D;
		fin >> D;
		int p[D];
		for (int i=0; i<D; i++) 
			fin >> p[i];
		fout << "Case #" << count << ": " << getAns(p, D) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}