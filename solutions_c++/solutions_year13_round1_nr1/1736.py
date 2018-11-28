#include <iostream>
using namespace std;

int main()
{
	int testN;
	cin >> testN;
	//scanf("%d", &testN);
	for (int testNumber = 1; testNumber <= testN; testNumber++)
	{
		long long count = 0;
		long long r, t;
		long long t1, t2;
		cin >> r >> t;
		//scanf("%ld%ld", &r, &t);

		t1 = r;
		t2 = r + 1;

		while ( ((t2 * t2) - (t1 * t1)) <= t)
		{
			t -= (t2 * t2) - (t1 * t1);
			count++;
			t2 += 2;
			t1 += 2;
		}

		printf("Case #%d: %ld\n", testNumber, count);
	}
}