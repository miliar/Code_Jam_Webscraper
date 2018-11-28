#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#pragma warning (disable : 4996)
int push(vector<bool>& num, const long long int& k)
{
	string s = to_string(k);
	int cnt = 0;
	for (char c : s)
		num[c - '0'] = true;
	for (bool b : num)
		if (b)
			cnt++;
	return cnt;
}
int main(int argc, char * argv[])
{
	FILE * fp = fopen("A-large.in", "r"), *fw = fopen("A-large.out", "w");
	int n; fscanf(fp, "%d", &n);
	for (int i = 1; i <= n; i++)
	{
		vector<bool> num(10, false);
		int k;  fscanf(fp, "%d", &k); long long int r = k;
		if (!k)
			fprintf(fw, "Case #%d: INSOMNIA\n", i);
		else
			while (1)
			{
				int chk = push(num, r);
				if (chk == 10)
				{
					fprintf(fw, "Case #%d: %lld\n", i, r);
					break;
				}
				r += k;
			}
	}
	return 0;
}