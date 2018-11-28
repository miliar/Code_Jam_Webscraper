#include <iostream>
#include <string>

using namespace std;

typedef long long llong;

int main()
{
	int T;
	string s, res;
	int t, i;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cin >> s;
		res = "";
		res += s[0];
		for(i=1; i<s.size(); i++)
		{
			if(s[i]>=res[0])
			{
				res = s[i] + res;
			}
			else
			{
				res = res + s[i];
			}
		}
		cout<< "Case #" << t << ": " << res << endl;
	}
}