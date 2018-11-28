
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	FILE *in;
	if (fopen_s(&in, "B-small-attempt0.in", "r+") != 0)
		printf("The in file was not opened\n");

	fstream out("B-small-attempt0.out", ios::out);
	if (out.bad())
		printf("The out file was not opened\n");

	int T;
	fscanf_s(in, "%d", &T);

	for (int tc = 1; tc <= T; tc++)
	{
		long long A, B, K;
		fscanf_s(in, "%lld %lld %lld\n", &A, &B, &K);

		long long sum = 0;
		for (long long i = 0; i < A; i++)
		{
			for (long long j = 0; j < B; j++)
			{
				if ( (i&j) < K)
					sum++;
			}
		}
	
		cout << "Case #" << tc << ": " << sum << endl;
		out << "Case #" << tc << ": " << sum << endl;
	}

	out.close();
	getchar();
}