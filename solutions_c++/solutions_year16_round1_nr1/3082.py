#include"stdafx.h"

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod2 1000000007

string str;
string st;

int main()
{
	int t, i, j,m,n,k;
	freopen("all.in", "r", stdin);
	freopen("out.txt", "w",stdout);


	cin >> t;
	j = 0;
	while (t--)
	{
		cin >> str;
		j++;
		st.clear();
		for (i = 0; i < str.size();i++)
		{
			if (i)
			{
				if (str[i] >= st[0])
					st.insert(0,1,str[i]);
				else
					st.push_back(str[i]);
			}
			else
				st.push_back(str[i]);

		//	cout << st << " ";



		}
		cout << "Case #" << j << ": ";
		cout << st << "\n";

	}


	return 0;
}