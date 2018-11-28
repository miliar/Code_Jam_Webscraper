#include <iostream>
#include <fstream>
using namespace std;

unsigned long countShip(unsigned long N) {
	bool counter[10], flag = false;
	for (int i = 0; i < 10; ++i) {
		counter[i] = false;
	}
	unsigned long j = 0;
	while (!flag)
	{
		j += N;
		for (int i = j; i > 0; i /= 10) {
			counter[i % 10] = true;
		}
		flag = counter[0];
		for (int i = 1; i < 10; ++i) {
			flag = flag && counter[i];
		}
	}
	return j;
}

int main(){
	int T;
	unsigned long N;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		if (N == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			cout << countShip(N) << endl;
		}
	}
	return 0;
}