#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

string getLastWord(string str)
{
	string res;
	for(size_t i = 0;i < str.size(); ++i)
		if(!i || str[i] >= res[0])
			res.insert(0, 1, str[i]);
		else
			res.push_back(str[i]);
	return res;
}

int main()
{
	int T;
	string str;
	cin >> T;
	for(int i = 1;i <= T; ++i)
	{
		cin >> str;	
		printf("Case #%d: ", i);
		cout << getLastWord(str) << endl;
	}
	return 0;
}
