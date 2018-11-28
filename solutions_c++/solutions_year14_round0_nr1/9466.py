#include <iostream>
#include <cstdio>
using namespace std;

int t, n1, n2;
int first[4][4], second[4][4];

int main()
{
	cin >> t;
	for(int k = 0; k < t; k++)
	{
		int temp1[4], temp2[4], ans;
		cin >> n1;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> first[i][j];
				if(i == (n1-1)) temp1[j] = first[i][j];
			}
		}

		cin >> n2;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> second[i][j];
				if(i == (n2-1)) temp2[j] = second[i][j];
			}
		}
		int cnt = 0;
		sort(temp1, temp1+4);
		sort(temp2, temp2+4);
		for(int i = 0; i < 4; i++)
		{
			if(binary_search(temp1, temp1+4, temp2[i])) 
			{
				ans = temp2[i];
				cnt++;
			}
		}
		if(cnt == 0) printf("Case #%d: Volunteer cheated!\n", k+1);
		else if(cnt == 1) printf("Case #%d: %d\n", k+1, ans);
		else if(cnt > 1) printf("Case #%d: Bad magician!\n", k+1);	
	}
	return 0;
}

