#include<iostream>

using namespace std;

int main()
{
	int a, b, k;
	int nCase;
	cin >> nCase;
	for (int z = 1; z <= nCase; ++z)
	{
		int count = 0;
		cin >> a >> b >> k;
		for (int i = 0; i < a; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				if ((i&j) < k)
					++count;
			}
		}
		cout << "Case #" << z << ": " << count << endl;
	}
	return 0;
}