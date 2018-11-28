#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <math.h>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int l = 0; l < t; ++l)
	{
		int n;
		cin>>n;
		if (n == 0)
		{
			cout<<"Case #"<<l + 1<<": INSOMNIA"<<endl;
			continue;
		}
		vector<bool> mas(10);
		for (int i = 0; i <= max(n * n, 100); ++i)
		{
			int c = (i + 1) * n;
			while (c > 0)
			{
				mas[c % 10] = true;
				c /= 10;
			}
			bool t = true;
			for (int j = 0; j < 10; ++j)
				t = (t && mas[j]);
			if (t)
			{
				cout<<"Case #"<<l + 1<<": "<<(i + 1) * n<<endl;
				break;
			}
			if (i == max(n * n, 100))
			{
				cout<<"Case #"<<l + 1<<": INSOMNIA"<<endl;				
			}
		}
	}
	return 0;
}