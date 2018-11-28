#include <algorithm>
#include <iostream>
using namespace std;

int arr[10000];
int main()
{
	int ts;
	cin >> ts;
	for (int ti = 1; ti <= ts; ti++)
	{
		int n, lim;
		cin >> n >> lim;
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
		}
		sort(arr, arr + n);
		int save = 0;
		for (int i = 0, j = n - 1; i < j; i++, j--)
		{
			while (j >= 0 && arr[i] + arr[j] > lim) j--;
			if (i < j && arr[i] + arr[j] <= lim) save++;
		}
		cout << "Case #" << ti << ": " << (n - save) << "\n";
	}
}
