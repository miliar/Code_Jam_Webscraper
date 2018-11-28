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
			// ������� ������ ����� ������
			n++;
			// ����� �������� ����� �� ����, �� �� 0-� ������� ������ ���� ���� �����.
			if (s[0] == '+') {
				// ���� �� 0-� ������� ������ ���, �� ����� ������� �������������� ��������.
				// ������� ����� ������� ������������������ �������� ����� � ����������� �
				n++;
				int k = 0;
				for (k; k < i; k++) {
					if (s[k] == '-') break;
					s[k] = '-';
				}
			}
			// ����������� ��������
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
