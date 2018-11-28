#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int cases = 0;
	cin >> cases;
	for(int k = 0;k<cases;k++)
	{
		string str;
		cin >> str;
		string ans = "";
		for(int i=0;i<str.length();i++)
		{
			if(0==ans.length()) ans = ans + str[i];
			else
			{
				if(str[i] >= ans[0]) ans = str[i] + ans;
				else ans = ans + str[i];
			}
		}

		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
