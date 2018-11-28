#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <math.h>


using namespace std;

int main()
{
	int test, D, k, index, max_k = -1, ans, min_ans;
	std::vector<int> v;
	cin >> test;
	for (int i=1; i<=test;i++)
	{	
		ans = 0;
		cin >> D;
		index = D;
		v.clear();
		while (index--)
		{	
			cin >> k;
			v.push_back(k);
			if (k > max_k)
				max_k = k;
		}
		for (int j=1;j<=max_k;j++)
		{	
			ans = 0;
			for (int l=0; l<D; l++)
			{
				// cout << "ceil = " << ceil(v[l]*1.0/j) << endl;
				ans = ans + ceil(v[l]*1.0/j) - 1;
			}
			ans = ans + j;
			// cout << "ans : " << ans;
			if (j == 1)
				min_ans = ans;
			if (ans < min_ans)
				min_ans = ans;
		}
		cout << "Case #" << i << ": " << min_ans << endl;
	}
	return 0;
}