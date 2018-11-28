#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	string left, right, s;
	char c;
	int n;
	ios_base::sync_with_stdio(false);
	cin >> n;
	for(int kase = 1; kase <= n; kase++)
	{
		cin >> s;
		c = s[0];
		left.clear();
		left.reserve(s.size());
		right.clear();
		right.reserve(s.size());
		left += c;
		for(int i = 1; i < s.size(); i++)
		{
			if(s[i] >= c)
			{
				left += s[i];
				c = s[i];
				//cerr<<'('<<c<<')';
			}
			else right += s[i];
		}
		cout << "Case #" << kase << ": ";
		//reverse(left.begin(), left.end());
		for(int i = left.size()-1; i >= 0; i--)
			cout << left[i];
		cout << right << endl;
	}
	return 0;
}