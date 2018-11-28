#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int t,x = 1,l,i,c,ans;
	char str[200],key;
	cin >> t;
	while(t--)
	{
		cin >> str;
		l = strlen(str);
		ans = 0;
		while(1)
		{
			key = str[0];
			i = 1;
			c = 0;
			while(i < l && str[i] == key)
			{
				i++;
				c++;
			}
			if(c == l-1 && str[0] == '+')
				break;
			for(i=0;i<=c;i++)
			{
				if(key == '+')
					str[i] = '-';
				else
					str[i] = '+';
			}
			ans++;
		}
		cout << "Case #" << x << ": " << ans << "\n";
		x++;
	}
	return 0;
}
