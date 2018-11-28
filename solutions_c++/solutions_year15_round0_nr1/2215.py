#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q1=0;q1<z;q1++) {
		int n;
		string s;
		cin >> n >> s;

		int res = 0;
		int count = 0;
		for (int i=0;i<n+1;i++) {
			if (count < i) {
				res += i - count;
				count = i;
			}
			count += s[i] - '0';
		}

		cout << "Case #" << (q1+1) << ": " << res << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}