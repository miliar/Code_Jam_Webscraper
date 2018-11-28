#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	int county = 0;
	while(t--)
	{
		county++;
		char a[100000];
		int n;
		int count = 0;
		int sum = 0;
		bool flag = true;
		cin >> a;

		n = strlen(a);

		for(int i = 0;i < n;i++)
		{
			if((a[i] == '-') && (i-count == 0) && (flag == true))
			{
				count++;

				if((i != n-1) && (a[i+1] != '+'))
				{	
					//cout << i << " " << "hello" << endl;
					continue;
				}
			}
			else
			{
				flag = false;
			}

			if((count > 0) && (a[i] != '+'))

			{
				sum += 1;
				count = 0;
				//cout << i << " "<<"Hello_1" << " " << sum << endl;
			}

			if((flag == false) && (a[i] == '-'))
			{
				//cout << i<< " "<<"Hello_2" << " " << sum << endl;
				if(i == n-1)
				{
					sum += 2;
				}
				if((i != n-1) && (a[i+1] == '+'))
				{
					sum += 2;
				}
			}
		}
		cout << "Case #" << county << ": "<< sum << endl;
	}

	return 0;
}
