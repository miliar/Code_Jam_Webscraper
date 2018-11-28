#include <iostream>
using namespace std;
int main()
{
	int T, i, j;
	cin>>T;
	string s, s1;
	for(i = 0;i<T;i++)
	{
		cin>>s;
		s1 = s[0];
		for(j=1;j<s.length();j++)
		{
			if(s[j]>=s1[0])
				s1 = s[j] + s1;
			else
				s1 = s1 + s[j];
		}
		cout << "Case #" << i + 1 << ": " << s1 << endl;
	}
	return 0;
}