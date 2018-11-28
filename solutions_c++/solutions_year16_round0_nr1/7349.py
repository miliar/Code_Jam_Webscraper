#include <iostream>
#include <fstream>
using namespace std;
bool andAr(bool *a, int n) {
	bool ret_val = true;
	for (int i = 0; i < n; i++) {
		ret_val &= a[i];
	}
	return ret_val;
}
void findDigits(long long N, bool *a) {
	while (N > 0) {
		a[N % 10] = true;
		N = N / 10;
	}
}
long long findLast(long long N, bool *a) {
	int i = 1;
	while (!andAr(a, 10)) {
		findDigits(i*N, a);
		if (i*N == (i + 1)*N) return -1;
		i++;
	}
	return (i-1)*N;
}
int main() {
	bool a[10];
	long long N;
	int T;
	ifstream input("ulaz.txt");
	ofstream output;
	output.open("izlaz.txt");
	input >> T;
	int i = 1;
	while (T-- > 0) {
		for (bool &b : a) {
			b = false;
		}
		input >> N;
		long long temp = findLast(N, a);
		if (temp != -1) {
			output << "Case #" << i << ": " << temp<<endl;
		}
		else {
			output << "Case #" << i << ": " << "INSOMNIA"<<endl;
		}
		i++;
	}
	output.close();
	getchar();
	return 0;
}