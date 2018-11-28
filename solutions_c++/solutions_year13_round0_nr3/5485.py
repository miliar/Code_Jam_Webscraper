#include <iostream>
using namespace std;
int mas[5]={1, 4, 9, 121, 484};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int a, b, res=0;
	for (int i=1; i<=t; i++)
	{
		cin >> a >> b;
		res=0;
		for (int j=0; j<5; j++)
			if (mas[j] >=a)
				if (mas[j]<=b)
					res++;
		cout << "Case #" << i << ": " << res << "\n";
	}
	return 0;
}