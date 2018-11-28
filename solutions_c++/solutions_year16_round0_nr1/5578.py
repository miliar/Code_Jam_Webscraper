#include <iostream>
#include <string>

using namespace std;

long long var[1000003];

void generate() {
	var[0] = -1;
	for (int i = 1; i <= 1000000; ++i) {
		bool num[10] = { false,false,false,false,false,false,false,false,false,false };
		int numbers = 10;
		long long counter = 1;
		long long temp; // value
		long long temp2; // devided by tens
		long long temp3; // mod
		while (numbers != 0) {
			temp = counter*i;
			counter++;
			temp2 = temp;
			while (temp2 > 0) {
				if (numbers == 0) break;
				temp3 = temp2 % 10;
				if (!num[temp3]) { numbers--; num[temp3] = true; }
				temp2 /= 10;
			}
		}
		var[i] = temp;
	}
}

int main() {
	generate();
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	int temp;
	for (int i = 1; i <= n; ++i) {
		cin >> temp;
		if (temp != 0) {
			cout << "Case #" << i << ": " << var[temp] << '\n';
		}
		else {
			cout << "Case #" << i << ": " << "INSOMNIA" << '\n';
		}
	}
	return 0;
}