#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
typedef long long lli;




int main()
{
	int t;
	cin >> t;
	for (int j=1;j<=t;j++)
	{
		int len;
		string seq;
		cin >> len >> seq;
		len++;
		int ans = 0, count = 0;

		for (int i = 0; i < len; ++i)
		{
			//cout << count << " " << i << endl;
			if (count >= i)
			{
				count += seq[i]-'0';
			}
			else if (seq[i]!='0')
			{
				ans += i-count;
				count += i-count+seq[i]-'0';
			}
		}
		
		cout << "Case #" << j;
		printf(": %d\n",ans);
	}





	return 0;
}