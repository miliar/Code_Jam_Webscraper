#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int first, second;
		int card[4][4];
		int chose[4];
		
		cin >> first;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				cin >> card[x][y];
		
		for (int x = 0; x < 4; x++)
			chose[x] = card[first-1][x];
			
		cin >> second;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				cin >> card[x][y];
				
				
		int count = 0;
		int ans = -1;
		for (int x = 0; x < 4; x++)
			for (int y = 0; y < 4; y++)
				if (chose[x] == card[second-1][y]) {
					count++;
					ans = chose[x];
				}
		cout << "Case #" << i+1 << ": ";	
		if (ans == -1)
			cout << "Volunteer cheated!" << endl;
		else if (count > 1)
			cout << "Bad magician!" << endl;
		else if (count == 1)
			cout << ans << endl;
	}
	return 0;
}