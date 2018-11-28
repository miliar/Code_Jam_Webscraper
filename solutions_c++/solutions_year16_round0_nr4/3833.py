#include <stdlib.h>
#include <string>
#include <assert.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

int main()
{
	int testCases;
	cin >> testCases;

	for (int i = 1; i <= testCases; i++)
	{
		int K;
		cin >> K;

		int C;
		cin >> C;

		int S;
		cin >> S;

		cout << "Case #" << i << ":";

		for (int j = 1; j <= S; j++)
			cout << " " << j;

		cout << endl;
	}
}