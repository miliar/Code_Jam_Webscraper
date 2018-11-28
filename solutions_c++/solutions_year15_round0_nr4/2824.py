#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	int x, r, c;
	string answer;
	
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		cin >> x >> r >> c;
		
		switch(x)
		{
			case 1:
				answer = "GABRIEL";
				break;
			case 2:
				if(r * c >= 2 && (r * c) % 2 == 0)
					answer = "GABRIEL";
				else
					answer = "RICHARD";
				break;
			case 3:
				if(r * c >= 6 && (r * c) % 3 == 0)
					answer = "GABRIEL";
				else
					answer = "RICHARD";
				break;
			case 4:
				if(r * c >= 12 && (r * c) % 4 == 0)
					answer = "GABRIEL";
				else
					answer = "RICHARD";
				break;
		}
		cout << "Case #" << i + 1 << ": " << answer << "\n";
	}
	
	return 0;
}