#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main()
{
	/*freopen("C:/Users/wanyunpeng/Desktop/in.in", "r", stdin);
	freopen("C:/Users/wanyunpeng/Desktop/out.txt", "w", stdout);*/
	//freopen("C:/Users/wanyunpeng/Desktop/large.in", "r", stdin);
	//freopen("C:/Users/wanyunpeng/Desktop/large-out.txt", "w", stdout);
	int cas;
	int i = 1;
	cin >> cas;
	while (cas--)
	{
		string str;
		cin >> str;
		string res = "";
		for (auto c : str)
		{
			if (res.empty())
				res += c;
			else
			{
				if (c >= res[0])
					res = c + res;
				else
					res += c;
			}
		}
		cout << "Case #" << i++ << ": " << res << endl;
	}
	return 0;
}