#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int fun(int n, string str)
{
	int currentClapping = str[0] - '0';// ����һ��ʼ�ͻ�վ�������Ƶ���
	int friends = 0;

	for (int i = 1; i < str.length(); i++)
	{
		// �����ǰ�ĺ��̶߳ȴ��ڹ��Ƶ��ˣ���Ҫ��һЩ���ѹ���
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