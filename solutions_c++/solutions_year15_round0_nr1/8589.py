#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t, tmp;
	int k, source = 0,req;
	string s;
	cin >> t;
	for(int j = 1; j <= t; j++)
	{
		cin >> k;
		cin >> s;
		req = 0	;
		source = s[0] - '0';
		for(int i = 1; i < s.size(); i++)
		{
			if(s[i]-'0') {
				if(source >= i)	 source += (s[i] - '0');
				else  { tmp = (i-source); req += tmp; source += (s[i] - '0' + tmp); } }
		}		
		cout << "Case #" << j << ": " << req << endl;
	}
	return 0;
}
