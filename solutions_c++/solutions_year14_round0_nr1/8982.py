#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n, array[8];
	vector<int> ans;
	
	cin >> n;
	
	for (int a = 0, b;a < n;a++)
	{
		ans.clear ();
		cin >> b;
		
		for (int x = 0, y;x < 4 * (b - 1);x++)
			cin >> y;
		
		for (int x = 0;x < 4;x++)
			cin >> array[x];
			
		for (int x = 0, y;x < 4 * (4 - b);x++)
			cin >> y;
		
		cin >> b;
		
		for (int x = 0, y;x < 4 * (b - 1);x++)
			cin >> y;
		
		for (int x = 0;x < 4;x++)
			cin >> array[4 + x];
			
		for (int x = 0, y;x < 4 * (4 - b);x++)
			cin >> y;
			
		sort (array, array + 8);
		
		for (int x = 0;x < 7;x++)
		{
			if (array[x] == array[x + 1])
				ans.push_back (array[x]);
		}
		
		if (ans.size () == 0)
			cout << "Case #" << a + 1 << ": Volunteer cheated!\n";
		else if (ans.size () > 1)
			cout << "Case #" << a + 1 << ": Bad magician!\n";
		else if (ans.size () == 1)
			cout << "Case #" << a + 1 << ": " << ans[0] << "\n";
	}
	
	return 0;
}