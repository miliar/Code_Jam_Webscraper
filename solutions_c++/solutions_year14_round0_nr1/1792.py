#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int row1[16], row2[16];
int ans1, ans2;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		cin >> ans1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int a;
				cin >> a;
				row1[a - 1] = i + 1;
			}
		cin >> ans2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int a;
				cin >> a;
				row2[a - 1] = i + 1;
			}
		
		int cnt = 0;
		int ans = -1;
		for (int i = 0; i < 16; i++)
			if (row1[i] == ans1 && row2[i] == ans2)
			{
				ans = i + 1;
				cnt++;
			}
		
		cout << "Case #" << caseI << ": ";
		if (cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else if (cnt > 1)
			cout << "Bad magician!" << endl;
		else
			cout << ans << endl;
	}
	
	return 0;
}
