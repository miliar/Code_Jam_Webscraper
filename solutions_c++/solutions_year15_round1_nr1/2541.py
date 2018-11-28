#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>

using namespace std;
int mushrooms[1000] = {0};

int method1(int N)
{
	int a, b;
	int count = 0;
	for (int i = 0; i < N - 1; i++) {
		a = mushrooms[i];
		b = mushrooms[i + 1];
		if (a > b)
			count += a - b;
	}
	return count;
}

int method2(int N)
{
	int a, b;
	int maxDiff = 0;
	int count = 0;
	int diff;
	int arr[1000] = {0};

	for(int i = 0; i < N - 1; i++) {
		a = mushrooms[i];
		b = mushrooms[i + 1];
		
		diff = a - b;

		if(maxDiff < diff)
			maxDiff = diff;
	}

	if (maxDiff == 0) return 0;
	for (int i = 0; i < N - 1; i++) {
		a = mushrooms[i];
		b = mushrooms[i + 1];
		if (a == 0) 
			continue;
		diff = a - b;

		if(diff < 0)
			if(a<maxDiff)
				count += a;
			else
				count += maxDiff;
		else if (a < maxDiff) 
			count += a;			
		else 
			count += maxDiff;
	}
	return count;
}

int main()
{
	int T;
	int N;
	int result1, result2;

	assert(scanf("%d", &T));
	for (int i = 0; i < T; i++) {
		assert(scanf("%d", &N));
		for (int j = 0; j < N; j++) {
			assert(scanf("%d", &mushrooms[j]));
		}
		result1 = method1(N);
		result2 = method2(N);
		printf("Case #%d: %d %d\n", i + 1, result1, result2);
	}
	return 0;
}
