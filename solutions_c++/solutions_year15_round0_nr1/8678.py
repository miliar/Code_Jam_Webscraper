#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main()
{
	int testcases;
	cin >> testcases;
	
	for(int j = 0; j < testcases; j++)
	{
		int shyness;
		string audience;
		cin >> shyness >> audience;

		int clappers = 0;
		int extra = 0;
		for(int i = 0; i <= shyness; i++)
		{
			int temp = (audience[i] - '0');

			if(i > clappers)
			{
				extra += i - clappers;
				clappers = i;
			}
			
			clappers += temp;
		}

		cout << "Case #" << j + 1 << ": " << extra << endl;
	}
}