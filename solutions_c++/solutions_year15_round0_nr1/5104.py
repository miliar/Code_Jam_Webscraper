#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int test, n, sum, add;
	string str;
	cin >> test;
	for(int x = 1; x <= test; x++)
	{
		cin >> n >> str;
		sum = (int)(str[0]-'0');
		add = 0;
		for(int i=1;i<str.size();i++)
		{
			if((sum < i)&&str[i]!='0')
			{
				add += i-sum;
				sum += i-sum;
			}
			sum += (int)(str[i] - '0');
			// cout << i << " " << sum << " " << (int)(str[i] - '0') << " " << add << endl;
		}
		cout << "Case #" << x << ": " << add << endl;
	}
	return 0;
}