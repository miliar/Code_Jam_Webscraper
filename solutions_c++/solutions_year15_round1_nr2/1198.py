#include <iostream>
#include <math.h>
#include <fstream>
#include <sstream>
using namespace std;

int N;
int B;
int M[100010];
int ans;

int check(long long int a) {
	long long int sum = 0;
	for (int i = 0; i < B; i++) {
		sum += floor((1.0*a)/M[i])+1;	
	}
	if (sum >= N) {
		int d = sum - N;
//		cout << sum << endl;
//		cout << "a" << a << " " << d << endl;
		for (int i = B-1; i >= 0; i--) {
			if (a%M[i] == 0) {
				d--;
				if (d < 0) {ans = i+1; return 0;}
			}
		}
	}
//	cout << sum << endl;
	if (sum < N) return 1;
//	if (sum==N-1) for (int i = 0; i < B; i++) if (a%M[i] == 0) {
//		ans = i; return 0;
//	}
//	if (sum==N) {//for (int i = 0; i < B; i++) if (a%M[i] == 0) {
//		ans = 0; return 0;
//	}
//	if (N-1 < sum) return -1;
//	return 1;
}

int main() {
	ifstream fin("in");
	ofstream fout("out");
	int T = 0;
	fin >> T;
	string l;
	for (int TT = 0; TT < T; TT++) {
		long long int a;
		fin >> B >> N;
		for (int i = 0; i < B; i++) fin >> M[i];
		double rate = 0.0;
		for (int i = 0; i < B; i++) rate += 1.0/M[i];
		a = floor((N-B-1)/rate);
//		cout << a << endl;
		ans = -1;
//		a = 0;
		int d = check(a);
		while (d != 0) {
			if (d > 0) a++;
			if (d < 0) a--;
			d = check(a);
		}
//		if (d > 0) while (d != 0) {a++; d = check(a);}
//		if (d < 0) while (d != 0) {a--; d = check(a);}
//		cout << "ans " << a << " " << ans << endl;
		fout << "Case #" << TT+1 << ": " << ans << endl;
//		return 0;
	}
	return 0;
}
