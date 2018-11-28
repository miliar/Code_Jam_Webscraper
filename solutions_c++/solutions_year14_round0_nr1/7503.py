#include <iostream>
using namespace std;

int n;
int cards1[4][4];
int cards2[4][4];
int main()
{
	cin >> n;
	int a, b;
	for (int i = 0; i < n; i++)
	{
			
		int set[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		cin >> a;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> cards1[j][k];
		cin >> b;	
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> cards2[j][k];
		for (int j = 0; j < 4; j++)
		//`		
				set[cards1[a-1][j]-1] = 1;
int count = 0;
		int ans;
		for (int j = 0; j < 4; j++)
			if (set[cards2[b-1][j]-1] == 1)
			{
				count ++;
				ans = cards2[b-1][j];
			}
		cout << "Case #" << i+1 << ": ";
		if (count == 0)
			cout <<  "Volunteer cheated!"<< endl;
		else if (count == 1)
			cout << ans << endl;
		else
			cout << "Bad magician!\n";
	}
}	
