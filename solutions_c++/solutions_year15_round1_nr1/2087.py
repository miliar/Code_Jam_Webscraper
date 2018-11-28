#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int test_num, n, arr[10050], y, z, m;

	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);

	cin >> test_num;
	for (int t = 1; t <= test_num; t++){
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> arr[i];
		}

		//sort(arr, arr + n);
		y = 0;
		m = 0;
		for (int i = 0; i + 1 < n; i++){
			if (arr[i] > arr[i + 1]){
				y += arr[i] - arr[i + 1];
				m = max(arr[i] - arr[i + 1], m);
			}
		}

		z = 0;
		for (int i = 0; i+1 < n; i++){
			z += min(arr[i], m);
		}

		cout << "Case #" << t << ": " << y << " " << z << endl;
	}
	return 0;
}