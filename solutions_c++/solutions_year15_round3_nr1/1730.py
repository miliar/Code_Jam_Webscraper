#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <fstream>
#include <ctime>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int T, R, C, W, ans, my_min, my_max;
int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
	clock_t t;
	t = clock();
	scanf("%d\n", &T);
	for (int kace = 1; kace <= T; ++kace)
	{
		cout << "Case #" << kace << ": ";
		scanf("%d %d %d\n", &R, &C, &W);
		my_min = min(R, C);
		my_max = max(R, C);
		ans = my_max/W;
		ans *= my_min;
		if(W <= my_min && my_max%W)
		{
			ans += (my_min/W);
			if(my_min%W)
				++ans;
		}
		else if(my_max%W)
				++ans;
		ans += (W - 1);
		cout<<ans <<endl;
	}
}
