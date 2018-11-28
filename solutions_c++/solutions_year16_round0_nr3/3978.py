#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<map>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;

void isPrime(long long n,long long* a)
{
	long long s = sqrt(n) + 1;
	for (long long i = 2; i != s; ++i) {
		if (n%i == 0)
		{
			a[0] = 0;
			a[1] = i;
			break;
		}
	}
	if (!a[1])
		a[0] = 1;
}

int main() {
	FILE *fin = freopen("C-small-attempt2.in", "r", stdin);
	//FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("C-small-attempt2.out", "w", stdout);
	//FILE *fout = freopen("B-large.out", "w", stdout);
	long long  T;
	cin >> T;
	long long N;
	long long J;
	cin >> N >> J;
	for (long long t = 1; t <= T; t++) {
		long long begin = pow(2, N - 1) + 1;
		long long end = pow(2, N) - 1;
		long long k = 0;
		vector<vector<long long>> result;
		vector<string> str(J,"");
		for (long long i = begin; i <= end; i++)
		{
			if ((i & 1) != 1) continue;
			long long num = i;
			vector <long long> vec;
			long long X[2] = { 0,0 };
			isPrime(num, X); // deal with base 2
			if (X[0]) // prime
				continue;
			else
				vec.push_back(X[1]);

			for (long long N = 3; N <= 10; N++)// deal with base 3, 4, ..., 9
			{
				long long NnaryVal = 0;
				long long number = i;
				long long base = 1;
				while (number)
				{
					NnaryVal += base*(number & (long long)1); // obtain the Nnary number val in 10 nary
					base = base*N;
					number = number >> 1;
				}
				X[0] = 0;
				X[1] = 0;
				isPrime(NnaryVal, X);
				if (X[0]) // this number is a prime
					break;
				else
					vec.push_back(X[1]);
			}
			if (X[0]) // some number between 3 and 9 is prime, then break
				continue;

			if (vec.size() == 9)// base 3--9 are all non prime numbers, then find one and push into results
				result.push_back(vec);
			while (num)
			{
				if (num & 1) str[k] +=  '1';
				else str[k] += '0';
				num = num >> 1;
			}
			reverse(str[k].begin(), str[k].end());

			k++;
			if (result.size() == J)
				break;
		}

		cout << "Case #" << t << ": "<<endl;
		for (long long i = 0; i < result.size(); i++)
		{
			cout << str[i] << " ";
			for (long long j = 0; j < 9; j++)
				cout<<result[i][j] << " ";
			cout << endl;
		}

	}
	exit(0);
}


//int main()
//{
//	int a[] = { 0,0 };
//	isPrime(16,a);
//	cout << a[0] << " " << a[1] << endl;
//	system("pause");
//	return 0;
//}