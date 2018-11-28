//Problem: Google Code Jam 2013 Round 1B A
//Name: Osmos
//Author: Bruce K. B. Tong
//Tag: Ad Hoc, Maths

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

#define SMALL
//#define LARGE

#define N_SIZE 100

#define a1d(a, n) for(int i=0; i<(int)(n); i++) {cout << a[i]; cout << endl;} cout << endl;

void read(int &A, int &N, int m[]) {
	cin >> A >> N;
	for (int i = 0; i < N; i++)
		cin >> m[i];
}

void print(int A, int N, int m[]) {
	cout << A << " " << N << endl;
	for (int i = 0; i < N; i++)
		cout << m[i] << " ";
	cout << endl;
}

int solve(int A, int N, int m[]) {
	int d[N_SIZE];
	sort(m, m+N);
	for (int i = 0; i < N-1; i++)
		d[i] = m[i+1]-m[i];
	int count = 0;
	for (int i = 0; i < N; i++)
		if (A > m[i]) {
			A += m[i];
		} else if (A != 1 && (A == m[i] || A+A-1 > m[i])) {
			count++;
			A = A+(A-1)+m[i];
		} else {
			if (A == 1) return count+(N-i);
			double r = ((double)m[i]-1)/(A-1);
			int k = ceil(log10(r)/log10(2.0));
			if (k == (int)(log10(r)/log10(2.0))) k++;
			if (k >= N-i) return count+(N-i);
			count += k;
			A = pow(2.0, k)*(A-1)+1+m[i];
		}
	return count;
}

int main() {
	freopen("A-sample.in", "rt", stdin);
	#ifdef SMALL
		freopen("A-small-attempt3.in", "rt", stdin);
		freopen("A-small-attempt3.out", "wt", stdout);
	#endif
	#ifdef LARGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif

	int T;				//1 <= T <= 100
	int A;				//1 <= A <= 100 (or 10^6)
	int N;				//1 <= N <= 10 (or 100)
	int m[N_SIZE];		//1 <= m[i] <= 100 (or 10^6)

	cin >> T;
	for (int i = 1; i <= T; i++) {
		read(A, N, m);
		//print(A, N, m);
		cout << "Case #" << i << ": ";
		cout << solve(A, N, m);
		cout << endl;
	}
	return 0;
}