#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("Input.in", "r", stdin);
	freopen("Output.out", "w", stdout);

	int t, i;
	cin >> t;

	for(i=1; i<=t; i++)
	{
		char temp;
		string s, compressed = "";
		cin >> s;

		int j = 0;
		while(j<s.size())
		{
			compressed += s[j];
			temp = s[j];
			
			while(s[j]==temp)
				j++;
		}

		int a[110];

		for(j=0; j<compressed.size(); j++)
		{
			if(compressed[j] == '-')
				a[j] = 0;
			else
				a[j] = 1;
		}

		int x, left, right, ans;

		if(compressed.size() == 1)
		{
			if(compressed[0] == '-')
				ans = 1;
			else
				ans = 0;
		}
		else
		{
			j = compressed.size() - 1;
			ans = 0;

			while(j >= 0)
			{
				while(a[j] == 1 && j >= 0)
					j--;

				if(j < 0)
					break;

				if(a[0] == 1)
				{
					a[0] = 0;
					ans++;
				}

				left = 0;
				right = j;

				while(left <= right)
				{
					x = !a[left];
					a[left] = !a[right];
					a[right] = x;
					
					left++;
					right--;
				}

				ans++;
			}
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	
	return 0;
}