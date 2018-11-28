#include <iostream>

using namespace std;

int main()
{
	int test = 0;
	cin >> test;
	for (int t = 1; t <= test; ++t){
		int n = 0, k = 0, s = 0;
		cin >> n >> k >> s;
		cout << "Case #" << t << ": ";
		for (int i = 1; i <= s; ++i)
			cout << i << " ";
		cout << endl;
	}

	return 0;
}
