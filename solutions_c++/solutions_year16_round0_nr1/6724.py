#include <iostream>
#include <fstream>

using namespace std;

bool done(bool A[]);
void mark(long long num, bool A[]);

int main() {
	int t, i;
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("sollarge.out");
	fin>>t;
	for (i=1;i<=t;i++) {
		bool A[10] = {0};
		long long n;
		fin>>n;
		fout<<"Case #"<<i<<": ";
		if (n==0) 
			fout<<"INSOMNIA\n";
		else {
			long long k = 1;
			while (!done(A)) {
				mark(n*k, A);
				k++;
			} 
			fout<<n*(k-1)<<endl;
		}
	}
	return 0;
}

bool done(bool A[]) {
	int i;
	for (i=0;i<10;i++) {
		if (A[i]==false)
			return false;
	}
	return true;
}

void mark(long long num, bool A[]) {
	while (num>0) {
		A[num%10] = true;
		num=num/10;
	}
	return;
}

