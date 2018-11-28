#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string>
#include <math.h>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	int n, J;
	cin>>n>>J;
	int c = 0;
	cout<<"Case #1: "<<endl;
	vector<int> mas(n);
	mas[0] = 1;
	mas[n - 1] = 1;
	while (c < J)
	{
		int cnt = 0;
		for (int i = 0; i < n; ++i)
		{
			cnt += mas[i];
		}
		if (cnt % 3 == 0)
		{
			mas[1] += 1;
			for (int i = 1; i < n - 1; ++i)
			{
				mas[i + 1]+= mas[i] / 2;
				mas[i] %= 2;
			}
			continue;
		}
		bool b = false;
		vector<long long> divs;
		for (int j = 2; j <= 10; ++j)
		{
			long long numb = 0;
			long long k = 1;
			for (int i = 0; i < n; ++i)
			{
				numb += k * mas[i];
				k *= j;
			}
			for (long long l = 2; l * l <= numb;  ++l)
			{
				if (numb % l == 0)
				{
					divs.push_back(l);
					break;
				}
			}
		}
		if (divs.size() == 9)
		{
			++c;
			for (int i = 0; i < n; ++i)
			{
				cout<<mas[n - i - 1];
			}
			cout<<" ";
			for (int i = 0; i < 9; ++i)
				cout<<divs[i]<<" \n"[i == 8];

		}
		mas[1] += 1;
		for (int i = 1; i < n - 1; ++i)
		{
			mas[i + 1]+= mas[i] / 2;
			mas[i] %= 2;
		}
	}

	return 0;
}