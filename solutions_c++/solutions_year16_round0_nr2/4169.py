#include"stdafx.h"

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod2 1000000007
#define asitis 1
#define change 0


vector<bool> cake;


int main()
{
	int t, i, j;ll n;
	freopen("bl.in", "r", stdin);
	freopen("out.txt", "w", stdout);


	scanf("%d", &t);
	string str;
	bool state;
	j = 0;
	while (t--)
	{
		j++;
		cin >> str;
		n = str.size();
		state = asitis;
		char check;
		int ans = 0;
		bool inside = false;
		for (i = n - 1; i >= 0; )
		{
			inside = false;
			if (state == asitis)
				check = '-';
			else
				check = '+';


				while ((i >= 0) && (str[i]==check))
				{
					inside = true;
					i--;
				}
				if (!inside)
					i--;
				else
				{
					ans++;


					state = !state;
				}

		}
		printf("Case #%d: %d\n", j, ans);


	}

	return 0;
}