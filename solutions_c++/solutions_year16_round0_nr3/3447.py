#include <iostream>
#include <cstring>
using namespace std;

int cnt = 0;
const int pro_N = 16;
const int pro_J = 50;

void answer(int num);
void bin(int num, char s[]);
long long int jin(char s[], int k);
int main()
{
	printf("Case #1:\n");

	for (int i = 0; cnt != pro_J; i++)
		answer(i);

	return 0;
}
void answer(int num)
{
	long long int res;
	int divisor[9] = { 0 };
	char data[pro_N+1] = "1";

	bin(num, data);
	data[pro_N-1] = '1';

	for (int i = 2; i <= 10; i++) {
		res = jin(data, i);

		if (res % 2 == 0) { divisor[i-2] = 2; }
		else {
			for (long long int j = 3; j*j <= res; j += 2) {
				if (res % j == 0) {
					divisor[i-2] = j;
					break;
				}
			}
		}
		if (divisor[i-2] == 0) return;
	}

	cnt++;
	printf("%s ", data);
	for (int i = 0; i < 9; i++)
		printf("%d ", divisor[i]);
	printf("\n");
}
void bin(int num, char s[])
{
	for (int i = pro_N-2; i >= 1; i--) {
		s[i] = num % 2 + '0';
		num /= 2;
	}
}
long long int jin(char s[], int k)
{
	long long int flag = 1;
	long long int result = 0;

	for (int i = strlen(s) - 1; i >= 0; i--) {
		result += (s[i] - '0') * flag;
		flag *= k;
	}

	return result;
}