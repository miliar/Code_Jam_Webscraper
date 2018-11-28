#include <iostream>
#include <new>

using namespace std;

int main(void)
{
	int t;
	int i;
	
	cin >> t;

	for (i = 0; i < t; i++)
	{
		int s_max;

		cin >> s_max;
		
		char * aud = new char[s_max+1];
		
		int j;
		
		for (j = 0; j < s_max+1; j++)
		{
			cin >> aud[j];
		}
		/*****************main algorithm*****************************************/
		int stand = 0;
		int need = 0;

		for (j = 0; j < s_max + 1; j++)
		{
			if (stand < j)
			{
				need += j - stand;
				stand += j - stand;
			}
			stand = stand + (aud[j] - '0');
		}

		cout << "Case #" << i+1 << ": " << need << endl;
		/************************************************************************/
		/*
		cout << s_max << " ";
		for (j = 0; j < s_max+1; j++)
		{
			cout << aud[j];
		}
		cout << endl;
		*/
		delete[] aud;
	}

	return 0;
}