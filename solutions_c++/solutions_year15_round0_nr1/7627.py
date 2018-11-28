#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int s_max;
	string s;
	int ans = 0;
	int people_std = 0;
	int c = 1;
	while(c <=T )
	{
		ans = 0;
		people_std = 0;

		cin>>s_max;
		cin>>s;
		people_std = s[0] - 48;

		for(int j=1; j<=s_max; j++)
		{
			if(people_std >= j)
				people_std += s[j] - 48;
			else
			{
				ans += (j - people_std);
				people_std = j + (s[j] - 48);
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
		}

return 0;
}
