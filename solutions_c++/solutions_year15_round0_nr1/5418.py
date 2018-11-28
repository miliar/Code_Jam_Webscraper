#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>


using namespace std;

int main()
{
	int t, k, test = 1;
	char ch;
	long long int cumulative = 0, maxlength, i, extra = 0;
	cin >> t;
	while (t--)
	{	
		cin >> maxlength;
		cumulative = 0;
		extra = 0;
		scanf("%c", &ch);
		for (i = 0; i<=maxlength; i++)
		{
			scanf("%c", &ch);
			k = ch - '0';
			if (i!=0)
			{
				if (i > cumulative + extra)
					extra = (i - cumulative);
			}			
			cumulative += k;
		}
		cout << "Case #" << test << ": " << extra << endl;
		test++;
	}
	return 0;
}