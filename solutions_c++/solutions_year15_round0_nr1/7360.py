#include<bits/stdc++.h>
using namespace std;

const int MAX = 1005;

int main()
{
	int test;
	cin>>test;
	int t = 0;
	while(test--)
	{
		t++;
		int S, i;
		char str[MAX];

		cin>>S >> str;

		int cnt = 0 , ans = 0;
		for(i = 0 ; i <= S ; i++ )
		{
			if(cnt >= i)
			{
				cnt = cnt+(str[i]-'0');
			}
			else if(str[i] != '0')
			{
				int var =  (i-cnt);
				ans += var;
		// 		cout<<"i "<<i <<" cnt "<<cnt<<" ans "<<ans<<" var"<<var<<endl;
				cnt += (str[i]-'0') + var;
			}

		}

		cout<<"Case #"<<t<<": "<<ans<<endl;

	}
}