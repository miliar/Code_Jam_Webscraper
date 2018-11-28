#include<iostream>
#include<memory.h>
using namespace std;

int main()
{
	freopen("A.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int v[17];
	int cs;
	int n,t,res,rescount;
	cin >> cs;
	for (int tc = 1; tc <= cs; tc++)
	{
		memset(v, 0, sizeof(v));
		rescount = 0;
		cin >> n;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> t;
				if (i + 1 == n)
				{
					v[t]++;
				}
			}
		}
		cin >> n;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> t;
				if (i + 1 == n)
				{
					if (v[t])
					{
						res = t;
						rescount++;
					}
				}
			}
		}
		cout << "Case #" << tc << ": ";
		switch (rescount)
		{
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		case 1:
			cout << res << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
		}

	}
	return 0;
}