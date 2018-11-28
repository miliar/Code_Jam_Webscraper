#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

using namespace std;

int countComp(string str)
{
	int k = 1;
	char cur = str[0];
	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] != cur)
		{
			k++;
			cur = str[i];
		}
	}
	return k;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	string str;
	getline(cin, str);
	for (int i = 1; i <= n; i++)
	{
		getline(cin, str);
		char end = str[str.size() - 1];
		int cnt = countComp(str);
		if (end == '+') cnt--;
		cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}