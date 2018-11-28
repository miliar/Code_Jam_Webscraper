#include <iostream>


using namespace std;

unsigned long long get_num(unsigned long long x) {
	bool visited[10];
	int number_visited = 0;
	for (int i = 0; i < 10; i++)
		visited[i] = false;


	for (unsigned long long i = 1; i < 10000; i++) {
		unsigned long long copy = i*x;

		while (copy > 0) {
			int cifra = copy % 10;
			if (visited[cifra] == false) {
				visited[cifra] = true;
				number_visited++;
			}
			copy /= 10;
		}

		if (number_visited == 10) return i*x;
	}
	return 0;
}

int main() {
	unsigned long long x;
	unsigned long long count;
	int T, t = 1;
	cin >> T;
	while (t <= T) {
		cin >> x;
		if (x == 0)
			cout << "Case #" << t << ": INSOMNIA" << endl;
		else {
			count = get_num(x);
			if (count > 0)
				cout << "Case #" << t << ": " << count << endl;
			else
				cout << "Case #" << t << ": INSOMNIA" << endl;	
		}
		t++;
	}
}