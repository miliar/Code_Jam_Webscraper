#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

void mysort(double *a, int n)
{
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n-i-1; j++) {
			if (a[j] > a[j + 1]) {
				double temp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = temp;
			}
		}
	}
}

int score_before(double *a, double *b, int n)
{
	if (n == 1) {
		if (a[0] > b[0])
			return 1;
		else
			return 0;
	}
	else {
		int curscore = 0;
		bool flag = false;
		for (int i = 0; i < n; i++) {
			if (b[i] > a[0]) {
				// delete b[i] from b
				for (int j = i; j < n - 1; j++)
					b[j] = b[j + 1];
				flag = true;
				break;
			}
		}
		if (flag == false)
			return n;
		else
			return score_before(++a, b, n - 1);
	}
	
	return 0;
}

int score(double *a, double *b, int n)
{
	bool flag = false;
	for (int i = 0; i < n; i++) {
		if (a[i] < b[i]) {
			flag = true;
			break;
		}
	}
	if (flag == false) return n;
	else {
		a++;
		score(a, b, n - 1);
	}
}

int main() {
	ifstream infile("D-small-attempt0.in");
	ofstream outfile("D-small-attempt0.out");
	unsigned int nCases;
	infile >> nCases;
	for (int i = 0; i < nCases; i++) {
		int N;
		infile >> N;
		double *A = new double[N];
		double *B = new double[N];
		double *C = new double[N];
		double *D = new double[N];
		for (int j = 0; j < N; j++)
			infile >> A[j];
		for (int j = 0; j < N; j++)
			infile >> B[j];
		// sort A and B
		mysort(A, N);
		mysort(B, N);
		for (int j = 0; j < N; j++)
			cout << A[j] << " ";
		cout << endl;
		for (int j = 0; j < N; j++)
			cout << B[j] << " ";
		for (int j = 0; j < N; j++) {
			C[j] = A[j];
			D[j] = B[j];
		}
		cout << endl;
		outfile << "Case #" << (i + 1) << ": ";
		outfile << score(A, B, N) << " " << score_before(C, D, N) << endl;
	}
	infile.close();
	outfile.close();
}

