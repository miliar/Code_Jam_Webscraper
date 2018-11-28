#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int matrix[4][4] = { 
	{ 1, 2, 3, 4 }, 
	{ 2, -1, 4, -3 }, 
	{ 3, -4, -1, 2 }, 
	{ 4, 3, -2, -1 } 
};

int mult(int a, int b)
{
	bool neg = false;
	if (a < 0) {
		a = -a;
		neg = true;
	}
	return neg ? -matrix[a - 1][b - 1] : matrix[a - 1][b - 1];
}

bool getK(int* arr, int start, int end)
{
	int c = 1;
	for (int i = start; i < end; i++) {
		c = mult(c, arr[i]);
	}
	return c == 4;
}

bool getJ(int* arr, int start, int end)
{
	int c = 1;

	for (int i = start; i < end - 1; i++)
	{
		c = mult(c, arr[i]);
		if (c == 3) {
			if (getK(arr, i + 1, end)) return true;
		}
	}
	return false;
}

bool getI(int* arr, int start, int end)
{
	int c = 1;

	for (int i = start; i < end - 2; i++)
	{
		c = mult(c, arr[i]);
		if (c == 2) {
			if (getJ(arr, i + 1, end)) return true;
		}
	}

	return false;
}


int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		
		int L, X;
		cin >> L >> X;
		cin.ignore();
		string s;
		getline(cin, s);

		int* arr = (int*)malloc(sizeof(int) * L * X);
		
		for (int i = 0; i < L * X; i++)
		{
			char c = s[i%L];
			arr[i] = c == '1' ? 1 : c=='i' ? 2 : c=='j' ? 3 : 4;
		}

		if (getI(arr, 0, L * X)) {
			cout << "Case #" << t << ": YES" << endl;
		}
		else {
			cout << "Case #" << t << ": NO" << endl;
		}

	}

	return 0;
}