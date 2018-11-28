#include <iostream>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
using namespace std;

int main()
{
	freopen("table", "r", stdin);
	freopen("test.out", "w", stdout);
	string str;
	int index = 0;
	cout << "Case #1: "<<endl;
	while (cin >> str)
	{
		index ++;
		cout << str;
		if (index == 10)
		{
			index = 0;
			cout << endl;
		}
		else
		{
			cout << ' ';
		}
	}
	return 0;
}