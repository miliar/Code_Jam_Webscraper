#include<iostream>
#include<vector>
#include<string.h>

int main()
{
	int n;
	//std::cin >> n;
	std::vector<int> myCase;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &n);
	int i; 
	for (i = 1; i <= n; i++)
	{
		int k;
		scanf("%d", &k);
	    //std::cin >> k;
		myCase.push_back(k);
	}
	int flag[10];
	for (i = 0; i < n; i++)
	{
		int N = myCase[i];
		if (N == 0) std::cout << "Case #" << i + 1 << ": INSOMNIA" << std::endl;
		else
		{
			int times = 1;
			memset(flag, 0, sizeof(flag));
			int count = 0;
			for (;count<10;times++)
			{
				int t = N*times;
				while (t > 0)
				{
					int digit = t % 10;
					t = t / 10;
					if (flag[digit] == 0){ flag[digit] = 1; count++; }
				}
			}
			std::cout << "Case #" << i + 1 << ": "<<N*(times-1)<<std::endl;
		}
	}
}
