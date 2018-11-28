#include <iostream>
#include <string.h>
using namespace std;
void flip(char str[], int until)
{
		for (int x = 0; x <= until; x++)
		{
			if (str[x] == '-')
				str[x] = '+';
			else
				str[x] = '-';
		}
}

int main()
{
	
		int cases;
		int flips, index, temp1, temp2;
		char set[101];
		int size;
		char pause;
		bool allup;
		cin >> cases;
		for (int x = 1; x <= cases; x++)
		{
			flips = 0;
			cin >> set;
			allup = false;
			size = strlen(set);
			index = 0;
			while (1)
			{
				for (temp1 = 0; set[temp1] == '+'; temp1++);
				for (temp2 = 0; set[temp2] == '-'; temp2++);
				if (size ==	temp1)
					break;
				if (temp1 > temp2)
					flip (set, temp1-1);
				else 
					flip (set, temp2-1);
				flips++;
			}
			cout << "Case #" << x << ": " << flips << endl;
		}
		return 0;
}

