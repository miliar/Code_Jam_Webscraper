#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;
int main()
{
	int t, tc = 1;
	scanf("%i", &t);
	while (t--)
	{
		int arr[] = {1, 4, 9, 121, 484};
		int a, b, cnt = 0;
		scanf("%i%i", &a, &b);
		for (int i = 0; i < 5; i++)
			if (arr[i] <= b && arr[i] >= a)
				cnt++;
		printf("Case #%i: %i\n", tc++, cnt);
	}
}
