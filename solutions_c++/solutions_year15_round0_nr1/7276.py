#include <bits/stdc++.h>
using namespace std;

int main()
{
	//ifstream cin("INPUT.txt");
	//ofstream cout("output.out");
	int t, y = 0;
	cin >> t;
	while(t--) {
		int s;
		string str;
		cin >> s;
		cin >> str;
		int extra = 0, sum = 0;
		for(int i = 1; i <= s; ++i) {
			sum += (str[i - 1] - '0');
			if(sum < i) {
				extra += (i - sum);
				sum += (i - sum);
			}
		}
		cout << "Case #" << ++y << ": " << extra << endl;
	}
	return 0;
}
