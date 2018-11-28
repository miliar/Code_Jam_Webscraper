#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		int a, b;
		cin >> a;
		int cards1[4];
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				int tmp;
				cin >> tmp;
				if(j+1==a)
					cards1[k] = tmp;
			}
		}
		cin >> b;
		int cards2[4];
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				int tmp;
				cin >> tmp;
				if(j+1==b)
					cards2[k] = tmp;
			}
		}
		int num = 0;
		int ans = 0;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if(cards1[j] == cards2[k])
				{
					num++;
					ans = cards1[j];
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(num==0)
			cout << "Volunteer cheated!";
		else if(num==1)
			cout << ans;
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
