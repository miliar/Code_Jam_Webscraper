
#include <iostream>
#include <string>

using namespace std;

int main()
{

	int T;

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		string buff;
		cin >> buff;
		int cost = 0;
		for(int i = (buff.length()-1); i >= 0; i--)
		{	
			if(buff[i] == '-')
			{
				for(int k = i; k >= 0; k--)
				{
					if(buff[k] == '-')
						buff[k] = '+';
					else if(buff[k] == '+')
						buff[k] = '-';
				}
				cost++;
			}
			
		}
		cout << "Case #" << t << ": ";
		cout << cost << endl;
	}
	

	return 0;
}


