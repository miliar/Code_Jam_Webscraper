#include <fstream>
#include <cassert>
#include <iostream>
using namespace std;

//#define DEBUG

const int v1 = 1;
const int vi = 2;
const int vj = 3;
const int vk = 4;

const int mul[5][5] = {
	{ 0,  0,  0,  0,  0},
	{ 0,  1, vi, vj, vk},
	{ 0, vi, -1, vk, -1*vj},
	{ 0, vj, -1*vk, -1, vi},
	{ 0, vk, vj, -1*vi, -1}
};

inline int multiply(int x, int y) {
	int sign = (x*y>0 ? 1 : -1);
	x = abs(x);
	y = abs(y);
	assert(x>0 && x<5);
	assert(y>0 && y<5);
	return sign * mul[x][y];
}

int power(int base, long long exp) {
	exp %=4;
	int product = 1;
	for (int i=1; i<=exp; i++) {
		product = multiply(product, base);
	}
	return product;
}

bool canFindAns(int a[], int L, long long X) {
	int whole = 1;
	for (int i=0; i<L; i++) 
		whole = multiply(whole, a[i]);
	if (power(whole, X) != -1) 
		return false;

#ifdef DEBUG
	cout << "whole = " << whole << endl;
#endif

	// find product to reduce i
	int ci = -1, pi = 0;
	int product = 1;
	for (int i=0; i<4; i++) {
		if (i+1 > X) 
			break;
		for (int j=0; j<L; j++) {
			product = multiply(product, a[j]);
			if (product == vi) {
				ci = i; 
				pi = j;
				break;
			}
		}
		if (ci != -1) break;
	}

	if (ci == -1) return false;

	int ck = -1, pk = 0;
	product = 1;
	for (int i=0; i<4; i++) {
		if (i+1 > X) 
			break;
		for (int j=L-1; j>=0; j--) {
			product = multiply(a[j], product);
			if (product == vk) {
				ck = i;
				pk = j;
				break;
			}
		}
		if (ck != -1) break;
	}

	if (ck == -1) return false;

	int need = ci + ck + (pi<pk ? 1 : 2);
	return need <= X;
}

int main() {
	ifstream fin("C-large.in");
	ofstream fout("pc_large.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int L;
		long long X;
		fin >> L >> X;
		if (X>11) {
			X = 12 + X % 4;
		}
		int a[L];
		for (int i=0; i<L; i++) {
			char c;
			fin >> c;
			if (c=='i') a[i]=vi;
			else if (c=='j') a[i]=vj;
			else if (c=='k') a[i]=vk;
			else assert(false);
		}

		#ifdef DEBUG
		for (int i=0; i<L; i++) {
			cout << a[i];
		}
		cout << endl;
		#endif

		fout << "Case #" << count << ": " << (canFindAns(a, L, X) ? "YES" : "NO") << endl;
	}
	fin.close();
	fout.close();
	return 0;
}