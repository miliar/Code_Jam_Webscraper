#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int case_num = 1; case_num <= T; case_num++)
	{
		long long r, t;
		cin >> r >> t;

		long long current_rad = r+1, old_rad = r;
		long long area = current_rad * current_rad - old_rad * old_rad;
		long long painted = 0;

		while (t >= area)
		{
			t -= area;
			painted++;
			current_rad += 2;
			old_rad += 2;
			area = current_rad * current_rad - old_rad * old_rad;
		}

		cout << "Case #" << case_num << ": ";
		cout << painted;
		cout << endl;
	}

	return 0;
}
