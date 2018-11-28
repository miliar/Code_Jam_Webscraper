#include <iostream>
using namespace std;

int main() {
	int t, n, ans, count;
	string shy;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		ans = 0;
		count = 0;
		cin >> n;
		cin >> shy;
		if (shy.length() != 1)
		{
			count = shy[0] - '0';
			for (int i = 1; i < shy.length(); i++)
			{
				if(count < i)
				{
					ans += ( i - count );
					count = i;
				}
				
				count+=( shy[i] - '0' );
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	// your code goes here
	return 0;
}