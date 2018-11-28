#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

vector<long long> num;
char buf[25];

bool check(long long num)
{
	sprintf(buf, "%lld", num);
	int len = strlen(buf);
	for (int i = 0; i < len / 2; i++)
		if (buf[i] != buf[len - 1 - i])
			return false;
	return true;
}

int main()
{
	for (int i = 1; i <= 100000000; i++)
		if (check((long long)i) && check((long long)i * i))
		{
			num.push_back((long long)i * i);
//			printf("%d %lld\n", i, (long long)i * i);
		}
//	printf("%d\n",(int)num.size());
	int totCas;
	scanf("%d", &totCas);
	for (int cas = 1; cas <= totCas; cas++)
	{
		long long A, B;
		scanf("%lld%lld", &A, &B);
		int cnt = 0;
		for (int i = 0; i < (int)num.size(); i++)
			if (num[i] >= A && num[i] <= B)
				cnt++;
		printf("Case #%d: %d\n", cas, cnt);
	}
	return 0;
}

