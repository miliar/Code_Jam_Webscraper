#include<iostream>
#include<fstream>
using namespace std;

bool allFound(bool *a) {
	for (int i = 0; i < 10; i++) {
		if (!a[i]) {
			return false;
		}
	}
	return true;
}

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("output.txt");
	int t;
	fin >> t;
	long long n;
	bool arr[10];
	for (int i = 1; i <= t; i++) {
		fin >> n;
		if (n == 0) {
			fout <<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		for (int i = 0; i < 10; i++) {
			arr[i] = false;
		}
		long long answer,temp,fa;
		for (long long j = 1; ; j++) {
			if (allFound(arr))	break;
			answer = n*j;
			fa = answer;
			temp = answer;
			while (answer > 0) {
				temp = answer % 10;
				arr[temp] = true;
				answer = answer / 10;
			}
		}
		fout << "Case #" << i << ": " << fa << "\n";
	}
	return 0;
}