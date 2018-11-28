#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	int cas;
	cin >> cas;
	for(int z=1; z<=cas; z++)
	{
		string str1;
		cin >> str1;
		string str2 = "";
		str2 += str1[0];
		for(int i=1; i<str1.length(); i++)
		{
			if(str1[i]>=str2[0])
				str2 = str1[i]+str2;
			else
				str2 += str1[i];
		}
		printf("Case #%d: ", z);
		cout << str2 << endl;
	}
	return 0;
}
