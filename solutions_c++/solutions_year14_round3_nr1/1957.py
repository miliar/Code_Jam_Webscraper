#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int main()
{
	int t;
	char s1[105];
	cin >> t;
	for(int i = 1;i <= t;++i)
	{
		cin >> s1;
		cout << "Case #" << i << ": ";
		int j, l = strlen(s1);
		long long p = 0, q = 0;
		for(j = 0;j < l;++j)
		{
			if(s1[j] == '/')
				break;
			p = (p*10) + (s1[j]-'0');
		}
		for(j++;j < l;++j)
		{
			if(s1[j] == '\0')
				break;
			q = (q*10) + (s1[j] - '0');
		}
		long long k;
		bool l1 = 0;
		for(k = 1;k < 40;++k)
			if((1 << k) == q)
			{
				l1 = 1; break;
			}
		if(l1)
		{
			q /= 2;
			if(p & 1)
			{
				if(p >= q)
					cout << 1 << endl;
				else
				{
					int ans = 1;
					while(p < q)
					{
						q /= 2;
						ans++;
					}
					cout << ans << endl;
				}
			}
			else
			{
				cout << "impossible\n";
			}
		}
		else
			cout << "impossible\n";
	}
	return 0;
}