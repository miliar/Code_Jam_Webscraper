#if 1
#include<iostream>
#include<stdio.h>
#include<conio.h>

using namespace std;
#define PI 1
int main()
{
	int T;
	long long int r, t;
	cin >> T;

	long long int numRings = 0;
	for (long long int caseNum = 0; caseNum < T; caseNum++)
	{
		numRings = 0;
		cin >> r >> t;

		for (long long int i = t; i - (2 * r + 1) >= 0; r += 2)
		{
			i -= (2 * r + 1);
			numRings++;
		}
		cout << "Case #" <<  caseNum+1 << ": " << numRings << endl;
	}
}
#endif