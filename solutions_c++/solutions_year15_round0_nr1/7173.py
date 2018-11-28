#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int fun(int n, string str)
{
	int currentClapping = str[0] - '0';// 这是一开始就会站起来鼓掌的人
	int friends = 0;

	for (int i = 1; i < str.length(); i++)
	{
		// 如果当前的害羞程度大于鼓掌的人，则要请一些朋友过来
		if (str[i] - '0' > 0 && i > currentClapping)
		{
			friends += i - currentClapping;
			currentClapping += i - currentClapping;
		}
		currentClapping += str[i] - '0';
	}




	return friends;
}

int main()
{
	int T;
	ifstream in("A-small-attempt0.in", ios::in);
	in >> T;

	ofstream out("result.out", ios::out);
	for (int i = 1; i <= T; i++)
	{
		int n; string str;
		in >> n >> str;

		int m = fun(n, str);

		out << "Case #" << i << ": " << m << endl;
	}

	return 0;
}