#include <iostream>

using namespace std;

int main() {

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int r, c, w, con;
		long long result;
		cin >> r >> c >> w;

		if (w == 1)
		{
			result = r * c;
		}
		else
		{
			con = (c - 2) / w;
			result = con * r;
			result += w;
			if (c % w == 1)
			{
				result++;
			}
		}
	
		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}