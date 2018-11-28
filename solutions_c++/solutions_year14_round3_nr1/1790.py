#include <stdio.h>
#include <iostream>

using namespace std;

unsigned long long int euclidean(unsigned long long int P, unsigned long long Q)
{
	if(Q == 0) return P;
	else return euclidean(Q, P%Q);
}

unsigned long long int binary_log(unsigned long long int x)
{
	int count = 0;
	while(x != 1)
	{
		count++;
		x = x >> 1;
	}
	return count;
}

unsigned long long int ancestor(unsigned long long int P, unsigned long long int Q)
{
	unsigned long long int gcd = euclidean(P, Q);
	P /= gcd;
	Q /= gcd;

	if(P == 1)
	{
		if(1 << binary_log(Q) != Q)	return -1;
		else return binary_log(Q);
	}
	else
	{
		if(1 << binary_log(Q) != Q)	return -1;
		else if(P*2 > Q) return 1;
		else return ancestor(P*2, Q) + 1;
	}
}

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		unsigned long long int P, Q;
		scanf(" %lld/%lld", &P, &Q);

		unsigned long long int gcd = euclidean(P, Q);
		P /= gcd;
		Q /= gcd;

		unsigned long long int result = ancestor(P, Q);
		if(result != (unsigned long long) -1) cout << result << endl;
		else cout << "impossible" << endl;
	}
}