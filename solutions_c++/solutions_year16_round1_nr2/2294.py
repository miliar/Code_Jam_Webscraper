#include<iostream>
#include<math.h>
#include<algorithm>
//#pragma warning(disable:4996)
using namespace std;
int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t,k;
	long long i, j, n;
	bool array[2501];
	cin >> t;
	int count = 1;
	while (t--)
	{
		cout << "Case #" << count << ": ";
		cin >> n;
		for (i = 0; i < 2501; i++)
			array[i] = false;
		for (i = 0; i < (2*n)-1 ; i++)
		{
			for (j = 0; j < n; j++)
			{
				cin >> k;
				array[k - 1] = !array[k - 1];
			}
		}
		for (i = 0; i < 2501; i++)
		{
			if (array[i] == true)
			{
				cout << i + 1 << " ";
			}
		}
			count++;
			cout << endl;
		}
	}
