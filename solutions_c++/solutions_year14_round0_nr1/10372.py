#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

#define Set(a,s) memset(a,s,sizeof(a))

using namespace std;

int main()
{
	int N;
	cin >> N;
	for(int caso = 1; caso <= N; caso++)
	{
		int a,b;
		int mx[8][8];
		int mx2[8][8];

		Set(mx,0);
		Set(mx2,0);

		cin >> a;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> mx[i][j];

		cin >> b;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> mx2[i][j];

		int ans=0;
		int ans2=0;

		for(int x = 1; x <= 4; x++)
		{
			int k = mx[a][x];
			for(int z = 1; z <= 4; z++)
			{
				if(k == mx2[b][z])
				{
					ans2 = k;
					ans++;
				}
			}
		}

		if(ans > 1)
			cout << "Case #"<<caso<<": Bad magician!"<<endl;
		else
			if(ans2)
				cout << "Case #"<<caso<<": "<< ans2<<endl;
			else
				cout << "Case #"<<caso<<": Volunteer cheated!"<<endl;
	}
	return 0;
}
