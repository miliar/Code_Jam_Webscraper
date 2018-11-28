#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int seen[10];

void resetseen() {
	for(int i=0; i<10; i++)
		seen[i] = 0;
}

void updateseen(long long n) {
	while(n>0) {
		seen[n%10] = 1;
		n /= 10;
	}
}

bool seenall() {
	for(int i=0; i<10; i++) {
		if(seen[i]==0) {
			return false;
		}
	}
	return true;
}

void printseen() {
	for(int i=0; i<10; i++)
		cout << seen[i] << " ";
	cout << endl;
}

long long getlast(long long N) {
	resetseen();
	for(long long m=1; m<=10; m++) {
		updateseen(m*N);
		if( seenall() ) {
			return m*N;
		}
		
	}
	return -1L;
}
long long getlast2(long long N) {
	resetseen();
	if(N==0)
		return -1L;
	long long M = N;
	printseen();
	while(true) {
		cout << M << ": ";
		updateseen(M);
		printseen();
		if(seenall()) {
			return M;
		}
		M += N;
	}
}

int main() {

	int T;
	long long N;
	fin >> T;
	for(int t=1; t<=T; t++) {
		fin >> N;
		long long sol = getlast2(N);
		fout << "Case #" << t << ": ";
		cout << "Case #" << t << ": " << N << " " << sol << endl;
		if(sol<0)
			fout << "INSOMNIA" << endl;
		else
			fout << sol << endl;
	}

	return 0;
}

