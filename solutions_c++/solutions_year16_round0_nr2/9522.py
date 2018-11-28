#include <iostream>
//#include <cstdio>
//#include <string>
//#include <algorithm>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

typedef long long ll;

using namespace std;

bool checkStack(char* stack) {
	while (*stack != '\0') {
		if (*stack == '-')
			return false;
		stack++;
	}
	return true;
}

int sameFirst(char* stack) {
	char a = *stack;
	stack++;

	int i = 1;

	while (*stack != '\0') {
		if (*stack != a)
			return i;
		stack++;
		i++;
	}
	return i;
}

void solveCase()
{
	char S[101];
	cin >> S;

	int m = 0;

	while (!checkStack(S)) {
		char s = S[0] == '+' ? '-' : '+';
		int aa = sameFirst(S);
		for (int i = 0; i < aa; i++)
		{
			S[i] = s;
		}
		m++;
	}

	cout << m;
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