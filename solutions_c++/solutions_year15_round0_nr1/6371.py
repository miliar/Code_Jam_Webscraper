

#include <bits/stdc++.h>
using namespace std;
int main()
{
freopen("A-large.in","r",stdin);
freopen("ans.out","w",stdout);
	
	int t, Min, total;
	string a;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> Min >> a;
		Min = total = 0;
		for (int j = 0; j < a.length(); j++)
		{
			if (j > total && a[j] != '0')
			{
				Min += j - total;
				total = j;
			}
			total += (a[j] - '0');
		}
		cout<<"Case #"<<i+ 1<<": "<<Min<<endl;
	}
return 0;
}
