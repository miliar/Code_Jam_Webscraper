#include <iostream>
using namespace std;

void countDigit(int count[], int n) {

	while (n > 0) {
		count[n % 10] = 1;
		n /= 10;
	}

}

void resetCountDigit(int count[]) {
	for (int i = 0; i < 10; ++i)
	{
		count[i] = 0;
	}
}

bool display(int count[]) {
	for (int i = 0; i < 10; i++)
	{
		if (count[i] == 0) {
			return false;
		}
	}

	return true;
}

int main() {
	int count[10] = {0};

	// for (int i = 0; i < 10; ++i)
	// {
	// 	cout << i << " : " << count[i] << endl;
	// }

	int size;
	cin >> size;

	int n, temp, loop;

	for (int i = 0; i < size; ++i)
	{
		cin >> n;
		loop = n;
		int j = 2;
		resetCountDigit(count);

		while (1) {
			temp = loop;
			countDigit(count, loop);

			if (display(count))
				break;

			loop = n * j++;

			if (loop == temp) {
				break;
			}
		}

		if (display(count)) {
			cout << "Case #" << i + 1 << ": " << loop << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA\n";
		}

		// for (int i = 0; i < 10; ++i)
		// {
		// 	cout << i << " : " << count[i] << endl;
		// }
	}

	return 0;


}