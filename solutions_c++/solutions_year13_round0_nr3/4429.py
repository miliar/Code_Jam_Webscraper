#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

bool isPalindrome(int long long x) {

	if (x<10) return true;

	int div = 1;
	while (x/div >=10) {
		div *= 10;
	}

	while (x) {
		int l = x/div;
		int r = x%10;
		if (l != r) return false;
		x = (x-div*l) /10;
		div /= 100;
	}
	return true;
}

int long long msqrt(int long long x) {
	double precision = 0.1;

	double long ix = x;
	double long xo = ix/2;
	double long diff = xo;
	double long x1;
	while (diff > precision) {
		x1 = (xo + ix/xo) /2 ;
		diff = abs(x1-xo);
		xo = x1;
	} 

	return xo;
}

int main() {
	fstream in, out;
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);

	int line_no;
	in >> line_no;
	for (int l = 1; l <=line_no; ++l) {
		int long long st, ed;
		in >> st, in >> ed;
		int long long mst = msqrt(st);
		int long long med = msqrt(ed)+1;
		int count=0;
		int long long i =0;
		if (mst *mst == st)
			i = mst;
		else 
			i = mst+1;

		for (; i <= med; ++i) {
			if (isPalindrome(i)) {
				int long long k = i*i;
				if (k > ed) break;
				if (isPalindrome(k))
					count++;
			}
		}
		out << "Case #" << l << ": " << count << endl;
		
	}

	in.close();
	out.close();
	return 0;

}