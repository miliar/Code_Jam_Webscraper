#include <iostream>
#include <string>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;

	cin >> t;
	for (int i=1; i<=t; i++) 
	{
		int s_max;
		cin >> s_max;
		cin.ignore();
		string people;
		cin >> people;
		int y = 0;
		int standing_people = 0;
		for (int s_level=0; s_level< people.length(); s_level++) 
		{
			int temp_y = 0;
			if (s_level > standing_people ) 
			{
				temp_y = s_level - standing_people;
				y += temp_y;
			} 
			standing_people += people[s_level] - '0' + temp_y; 
		}
		cout << "Case #" << i << ": " << y << endl;
	}
}