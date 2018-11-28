#include <stdio.h>
#include <iostream>=
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
#pragma warning (disable: 4996)
int getDiv(const vector<bool>& v)
{
	int ret = 0;
	bool bb = v.front();
	for (bool b : v)
	{
		if (b != bb)
			ret++;
		bb = b;
	}
	return ret;
}
int main()
{
	FILE * fp = fopen("B-large.in", "r"), *fw = fopen("B-large.out", "w");
	int n; fscanf(fp, "%d\n", &n);
	for (int i = 1; i <= n; i++)
	{
		char ch = 0;
		vector<bool> v;
		do {
			fscanf(fp, "%c", &ch);
			if (ch != '\n')
				v.push_back(ch == '+' ? true : false);
		} while (ch != '\n');
		v.push_back(true);

		fprintf(fw, "Case #%d: %d\n", i, getDiv(v));
	}
	return 0;
}