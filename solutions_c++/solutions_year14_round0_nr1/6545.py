#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int t = 1 ;t <= n ;t++)
	{
		int r1;
		cin >> r1;
		int count1[17]= {0};
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int temp;
				cin >> temp;
				if(i==r1)
				{
					count1[temp]++;
				}

			}
		}

		int r2;
		cin >> r2;
		int count2[17]= {0};
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int temp;
				cin >> temp;
				if(i==r2)
				{
					count2[temp]++;
				}

			}
		}

		int count = 0;
		int ans;
		for(int i=1;i<=16;i++)
		{
			if(count1[i]== 1 and count2[i]==1)
			{
				ans = i;
				count++;
			}
		}

		cout << "Case #"<<t<<": ";
		if(count == 1)
			cout << ans<<endl;
		else if(count == 0)
			cout << "Volunteer cheated!"<<endl;
		else
			cout << "Bad magician!"<<endl;
	}
}