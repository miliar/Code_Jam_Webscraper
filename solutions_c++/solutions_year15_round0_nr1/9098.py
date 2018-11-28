#include <iostream>
#include <string>

using namespace std;

int main ()
{
	int T;
	cin >> T;
	for(int i = 0; i<T; i++)
	{
		int S;
		cin >> S;
		int clapping = 0, draugu = 0;
		for(int j = 0; j<=S; j++)
		{
			char curr;
			cin >> curr;
			if(clapping >= j)
			{
				//cout << "setting clapping from " << clapping << " to " << clapping + int(curr) - 48<< endl;
				clapping = clapping + int(curr) - int('0');
			}
			else
			{
				draugu = draugu + j - clapping;
				clapping = j + int(curr) - int('0');
			}
		}
		cout << "Case #" << i+1 << ": " << draugu << endl;
	}
}
