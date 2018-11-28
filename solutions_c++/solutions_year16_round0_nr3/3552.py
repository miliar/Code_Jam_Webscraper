#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
#pragma warning (disable: 4996)

vector<long long int> getPrimes(long long int N) {
	vector<long long int> ret;

	if (N >= 2) ret.push_back(2);
	if (N >= 3) ret.push_back(3);

	long long int i, j, k;

	bool ctn = true;
	long long int mid_point = (long long int)sqrt(N - 1) / 6 + 1;

	for (i = 1; ctn && i <= mid_point; i++) {
		for (j = -1; j <= 1; j += 2) {
			long long int now = i * 6 + j;

			if (now > sqrt(N)) {
				ctn = false;
				break;
			}

			bool flag = true;
			for (auto here : ret) {
				if (now % here == 0) {
					flag = false;
					break;
				}

			}
			if (flag) {
				ret.push_back(now);
			}
		}
	}

	ctn = true;

	long long int ret_sqrt_cnt = (int)ret.size();
	for (i = mid_point - 2; ctn && i <= (N - 1) / 6 + 1; i++) {
		for (j = -1; j <= 1; j += 2) {
			long long int now = i * 6 + j;
			if (now <= ret[ret_sqrt_cnt - 1]) continue;
			if (now > N) {
				ctn = false;
				break;
			}

			bool flag = true;
			for (k = 0; k<ret_sqrt_cnt; k++) {
				if (now % ret[k] == 0) {
					flag = false;
					break;
				}
			}
			if (flag) {
				ret.push_back(now);
			}
		}
	}
	return ret;
}
long long int isPrime(long long n, const vector<long long> v) {
	for (auto now : v)
		if (n % now == 0) 
			return now;
	return 0;
}
long long int isPrime(long long int n) {
	return isPrime(n, getPrimes((int)sqrt(n)));
}
long long int getPrimefactor(long long int n)
{
	if(!(n%2))
		return 2;

	for (int i = 3; i <= sqrt(n); i = i + 2)
		while (n%i == 0)
			return i;

	if (n > 2)
		return 0;
}
long long int convert(const vector<bool>& v, int base)
{
	long long int ret = 0, dep = 0;
	long long int ddd = 1;
	for (vector<bool>::const_reverse_iterator it = v.rbegin(); it != v.rend(); ++it)
	{
		ret += ((*it) ? 1 : 0) * (ddd);
		ddd *= base;
	}
	return ret;
}
void next(vector<bool>& v)
{
	int cnt = 0;
	for (vector<bool>::reverse_iterator it = v.rbegin(); it != v.rend(); ++it)
		if (!(*it))
		{
			(*it) = true;
			for (vector<bool>::reverse_iterator iit = v.rbegin(); iit != it; ++iit)
				(*iit) = false;
			break;
		}
		else
			cnt++;
	if (!cnt)
		v[0] = v[v.size() - 1] = true;
	if (!v[v.size() - 1])
		next(v);
}
int main(int argc, char * argv[])
{
	FILE * fp = fopen("C-small-attempt2.in", "r"), *fw = fopen("C-small-attempt2.out", "w");
	int t,n,k; fscanf(fp, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		fscanf(fp, "%d %d", &n, &k);
		int cnt = 0, ctt = 0;
		vector<bool> v(n, false);
		fprintf(fw, "Case #%d:\n", i);
		do {
			vector<long long int> ret;
			do {
				next(v);
				ret.assign(9, 0); cnt = 0;

				for (int j = 2; j <= 10; j++) 
					ret[j - 2] = getPrimefactor(convert(v, j));

				for (long long int e : ret)
					if (e)
						cnt++;
			} while (cnt < 9);
			for (bool e : v)
				fprintf(fw, "%c", e ? '1' : '0');
			for (long long int e : ret)
				fprintf(fw, " %lld", e);
			fprintf(fw, "\n");
		} while (++ctt < k);
	}
	return 0;
}