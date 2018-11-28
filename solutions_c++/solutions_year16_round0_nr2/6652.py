#include "iostream"
#include "cstdio"
#include "string"

using namespace std;

int main()
{
	// freopen("data.in", "r", stdin);
	// freopen("data.out", "w", stdout);
	int T, cnt = 0;
	string s;
	cin >> T;
	while(T--)
	{
		cnt++;
		cin >> s;
		int len = s.length(), num = 1, result;
		char flag = s[0];
		for(int i = 1; i < len; i++)
			if(s[i] != flag)
			{
				num++;
				flag = s[i];
			}
		if(num % 2 == 0)
			result = (s[0]=='+') ? num : num-1;
		else
			result = (s[0]=='+') ? num-1 : num;
		cout << "Case #" << cnt << ": " << result << endl;
	}
	return 0;
}