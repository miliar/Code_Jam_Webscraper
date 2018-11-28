#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>


using namespace std;

int main()
{
	int k, test;
	long long int standing = 0;
	long long int Smax, i;
	long long peopleReq = 0;
	char ch;
	cin >> test;
	for (int j = 1; j<=test; j++)
	{	
		cin >> Smax;
		standing = 0;
		peopleReq = 0;
		scanf("%c", &ch);
		for (i = 0; i<=Smax; i++)
		{
			scanf("%c", &ch);
			k = ch - '0';
			if !(i==0)
			{
				if (i > standing + peopleReq)
					peopleReq = i - standing;
			}			
			standing = standing + k;
		}
		cout << "Case #" << j << ": " << peopleReq << endl;
	}
	return 0;
}