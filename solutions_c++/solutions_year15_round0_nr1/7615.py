// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <vector>

int T;
int k;
char str[100];

int getResult()
{
	std::vector<int> v;

	for (int i = 0; i <= k; i++) {
		v.push_back(str[i] - '0');
	}

	int sum   = 0;
	int count = 0;
	for (int i = 0; i < v.size(); i++) {
		if (sum < i) {
			int tcount = (i - sum);
			sum   += tcount;
			count += tcount;
		}
		sum += v[i];
		if (sum > k) break;
	}

	return count;
}

int main()
{
	FILE* fp = fopen("input.txt", "r");

	fscanf(fp, "%d\n", &T);
	for (int i = 0; i < T; i++) {
		fscanf(fp, "%d %s", &k, str);
		printf("Case #%d: %d\n", i + 1, getResult());
	}
	
	return 0;
}

