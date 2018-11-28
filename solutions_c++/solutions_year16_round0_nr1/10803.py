#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>

using namespace std;

const int checker = 0x000003FF;

int getBit(int num) {
	if (num == 9) return (1 << 9);
	if (num == 8) return (1 << 8);
	if (num == 7) return (1 << 7);
	if (num == 6) return (1 << 6);
	if (num == 5) return (1 << 5);
	if (num == 4) return (1 << 4);
	if (num == 3) return (1 << 3);
	if (num == 2) return (1 << 2);
	if (num == 1) return (1 << 1);
	if (num == 0) return (1 << 0);

	return getBit(num / 10) | getBit(num % 10);
}

int solveFunc(const int& in)
{
	if (in == 0) return -1;

	bool b[10] = { false, };
	int bit = 0;

	for (int i = 1; i < 101; ++i) {
		const int num = in * i;
		bit |= getBit(num);
		if ((checker & bit) == checker)
			return num;
	}

	return -1;
}

int main(int argc, char* argv[])
{
	int in = -1;
	int ret = -1;
	size_t max = 0;
	size_t cnt = 1;

	cin >> max;

	while (!cin.eof()) {
		cin >> in;

		if (cin.fail())
			break;

		if (in >= 0 && in <= 1000000)
			ret = solveFunc(in);

		if (ret == -1)	cout << "Case #" << cnt << ": INSOMNIA" << endl;
		else				cout << "Case #" << cnt << ": " << ret << endl;

		if (cnt >= max)
			break;

		++cnt;
		ret = -1;
		in = -1;
	}

	return 0;
}