#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q1=0;q1<z;q1++) {
		int n;
		cin >> n;

		vector<bool> seen(10, false);
		int last = -1;
		for (int i=1; i<=100;i++) {
			int num = i * n;
			while (num > 0) {
				seen[num%10] = true;
				num /= 10;
			}

			bool flag = true;
			for (int j=0;j<10;j++) {
				if (!seen[j]) {
					flag = false;
					break;
				}
			}
			
			if (flag) {
				last = i * n;
				break;
			}
		}

		cout << "Case #" << (q1+1) << ": ";
		if (last == -1) 
			cout << "INSOMNIA" << endl;
		else
			cout << last << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}