#include <iostream>
#include <vector>
#include <string>

using namespace std;

void test()
{
	string s;
	cin >> s;
	int n = 0;
	for (int i = s.length() - 1; i >= 0; i--) {
		if (s[i] == '-') {
			// находим первый минус справа
			n++;
			// чтобы заменить минус на плюс, то на 0-й позиции должен быть тоже минус.
			if (s[0] == '+') {
				// если на 0-й позиции минуса нет, то нужно сделать дополнительную операцию.
				// находим самую длинную последовательность плюсиков слева и инвертируем её
				n++;
				int k = 0;
				for (k; k < i; k++) {
					if (s[k] == '-') break;
					s[k] = '-';
				}
			}
			// инвертируем блинчики
			for (int j = 0; j <= i; j++) {
				s[j] = s[j] == '+' ? '-' : '+';
			}
			for (int j = 0; j <= i / 2; j++) {
				int k = i - j;
				swap(s[j], s[k]);
			}
		}
	}
	cout << n;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
