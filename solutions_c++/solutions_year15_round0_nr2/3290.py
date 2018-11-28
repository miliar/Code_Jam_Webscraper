#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("2.out" , "w" , stdout);
	int t , count;
	cin >> t;
	for(count = 1; count <= t ;count++)
	{
		int n ,i ,x ,j;
		cin >> n;
		int hash[1009] = {0} , total[1009] = {0};
		for(i = 0;i < n;i++)
		{
			cin >> x;
			hash[x]++;
		}
		for(i = 1;i <= 1000;i++)
		{
			for(j = 1;j <= 1000 ; j++)
			{
				if(j%i == 0)
					total[i] += hash[j] * (j/i - 1);
				else
					total[i] += hash[j] * (j/i);
			}
			total[i] += i;
		}
		int min = INT_MAX;
		for(i = 1;i < 1001;i++)
		{
			if(total[i])
			{
				if(min > total[i])
					min = total[i];
			}
		}
		cout << "Case #" << count << ": " << min << endl;
	}
	return 0;
}