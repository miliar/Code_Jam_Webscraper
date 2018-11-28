#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string str, new_str;

int main()
{
	ll t, i, j, n, m, len, tc;

	scanf("%lld", &t);

	for(tc=1;tc<=t;++tc)
	{
		cin>>str;

		new_str = "";

		len = str.length();

		new_str.push_back(str[0]);

		for(i=1;i<len;++i)
		{
			if(str[i]>=new_str[0])
			{
				//new_str.push_front(str[i]);
				new_str = str[i] + new_str;
			}
			else
			{
				new_str.push_back(str[i]);
			}
		}

		cout<<"Case #"<<tc<<": ";

		cout<<new_str<<endl;
	}

	return 0;
}