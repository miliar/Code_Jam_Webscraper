#include<iostream>
#include<algorithm>
using namespace std;
int a[5][5];
int b[5][5];
int num[17];

int main()
{
	int T, ans1, ans2;
	cin >> T;
	while (T--)
	{
		memset(num, 0, sizeof(num));
		cin >> ans1;
		for (int i = 1; i < 5;i++)
		{
			for (int j = 1; j < 5; j++)
			{
				cin >> a[i][j];
			}
		}
		cin >> ans2;
		for (int i = 1; i < 5; i++)
		{
			for (int j = 1; j < 5; j++)
			{
				cin >> b[i][j];
			}
		}
		
		for (int i = 1; i < 5; i++)
		{ 
			num[a[ans1][i]]++;
			num[b[ans2][i]]++;
		}
		int times = 0;
		int answer = 0;
		for (int i = 1; i <= 16;i++)
		{
			if (num[i]==2)
			{
				answer = i;
				times++;
			}
		}
		if (times == 0)
		{
			cout << "Case #" << 3 - T<<": " << "Volunteer cheated!" << endl;
		}
		else if (times == 1)
		{
			cout << "Case #" << 3 - T << ": " << answer << endl;
		}
		else
		{
			cout << "Case #" << 3 - T << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}