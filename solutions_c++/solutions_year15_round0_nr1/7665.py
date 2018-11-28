#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int tc = 0, res = 0;
	int smax = 0;
	char shy[2000];
	scanf("%d",&tc);

	for (int i = 1; i <= tc; i++)
	{
		res = 0;
		scanf("%d %s", &smax, shy);

		int pplsofar = 0;
		
		pplsofar = shy[0] - '0';
		for (int j = 1; j <= smax; j++)
		{
			int p = shy[j] - '0';
			if (pplsofar < j)
			{
				res += (j - pplsofar);
				pplsofar += (j - pplsofar) + p;	
			}
			else
			{
				pplsofar += p;
			}
		}	
		
		cout << "Case #" << i << ": " << res << endl;		
	}

	return 0;
}
