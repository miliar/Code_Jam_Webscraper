#include <iostream>
//#include <cstdio>
//#include <string>
//#include <algorithm>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

typedef long long ll;

using namespace std;

void solveCase()
{
	int N;
	cin >> N;

	if (N == 0) {
		cout << "INSOMNIA";
		return;
	}

	int digits[10];
	for (int i = 0; i < 10; i++)
		digits[i] = 0;

	char str[30];

	for (int i = 1; i < 1000000; i++)
	{
		sprintf(str, "%d", N*i);
		int ind = 0;
		while (str[ind] != '\0') {
			digits[str[ind] - '0'] = 1;
			ind++;
		}

		int res = 0;
		for (int j = 0; j < 10; j++)
		{
			res += digits[j];
		}
		if (res == 10) {
			cout << i*N;
			return;
		}
	}

}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 0; c < cases; c++)
	{
		cout << "Case #" << c + 1 << ": ";
		solveCase();
		cout << endl;
	}
}