//Standing Ovation
#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int m = 1 ; m <=t ; m++)
	{
		int max;
		cin >> max;
		string str;
		cin >> str;
		int cnt = str[0]-'0';
		int ans = 0;
		for(int i = 1 ; i < int(str.size()) ;i++)
		{
			if(i > cnt)
			{
				ans += (i-cnt);
				cnt = i;
			}
			
			cnt += str[i] - '0';
		}
		cout << "Case #" << m << ": " << ans << endl;
	}
}