#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, l, count, j;
	string s;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> s;
		l = s.size();
		count = 0;
		for(j = 1; j < l; j++)
			if(s[j - 1] != s[j])
				count++;
		if(s[l - 1] == '-')
			count++;
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}

