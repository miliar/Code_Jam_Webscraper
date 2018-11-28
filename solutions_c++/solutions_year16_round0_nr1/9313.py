#include <iostream>
#include <fstream>

using namespace std;
void printResult(long long int *arr, int n) {
	ofstream file("a.out");
	for (int i = 0; i < n; i++) {
		if (arr[i] == 0) {
			file << "Case #" << i + 1 << ": INSOMNIA";
		}
		else {
			file << "Case #" << i + 1 << ": " << arr[i];
		}
		file << endl;
	}
	file.close();
}
bool validate(bool arr[], int k) {
	while (k > 0) {
		arr[k % 10] = true;
		k /= 10;
	}
	for (int i = 0; i < 10; i++) {
		if (!arr[i]) return false;
	}
	return true;
}
int main() {
	ifstream file("i.in");

	bool arr[10];
	int n, i;
	long long int k, *res;
	file >> n;
	res = new long long int[n];

	for (int ii = 0; ii < n; ii++) {
		i = 1;
		for (int i = 0; i < 10; i++) arr[i] = false;
		file >> k;
		if (k == 0) {
			res[ii] = 0;
		}
		else {
			while (!validate(arr, k*i++)) {}
			res[ii] = k*(i - 1);
		}
	}
	file.close();
	printResult(res, n);
	return 0;

}