#include <cstdio>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int T;
int A, B, K;


void do_case(int index)
{
	cin >> A >> B >> K;
	int num = 0;

	for (int i = 0; i < A; ++i) 
	{
		for (int j = 0; j < B; ++j) 
		{
			int c = i & j;
			if (c < K) {
				num++;
			}
		}
	}

	printf("Case #%d: %d\n", index + 1, num);
}

int main()
{
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		do_case(i);
	}

	return 0;
}