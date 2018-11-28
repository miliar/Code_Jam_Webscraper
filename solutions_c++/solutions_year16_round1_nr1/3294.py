#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	int i;
	string s;
	for (i=1;i<=T;i++)
	{
		cin>>s;
		string o = "";
		o = s[0];
		int len = s.length();
		int j;
		for (j=1;j<len;j++)
		{
			if (s[j] >= o[0])
				o = s[j] + o;
			else
				o = o + s[j];
		}
		cout << "Case #" << i << ": " << o << endl;
	}
	return 0;
}
