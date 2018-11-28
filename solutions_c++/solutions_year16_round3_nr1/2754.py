#include <iostream>
#include <math.h>
using namespace std;


int twoleft(int *p, int n)
{
	int t = 0, i, x, y;
	for(i = 0; i < n; ++i)
	{
		if(p[i])
			++t;
	}	
	if(t == 2)
	{
		x = y = 0;
		for(i = 0; i < n; ++i)
		{
			if(p[i])
			{
				if(x == 0) {x = i; continue;}
				if(y == 0) y = i;
			}
		}

		for(i = 0; i < p[x]; ++i)
		{
			cout << " " << ((char)('A'+x)) << ((char)('A'+y));	
		}	
		
		return 1;
	}
	return 0;
}
int main()
{
	int t, n, p[26] = {0}, i, j, k, tt, m, total, pi;
	cin >> tt;
	for(t = 1; t <= tt; ++t)
	{
		cout << "Case #" << t << ":";
 
		cin >> n;
		total = 0;
		for(i = 0; i < n; ++i)
		{
			cin >> p[i];
			total += p[i];
		}

		while(total)
		{
			if(twoleft(p, n))
			{				
				break;	
			}
			
			for(i = 0; (i < n); ++i)				
			{
				if(p[i])
				{
					p[i] -= 1;
					m = ((total-1)/2) + 1;
					
					for(j = 0; j < n; ++j)
					{
						if(p[j] >= m)
						{
							break;
							
						}
					}
					if(j == n)
					{
						total -= 1; 
						cout << " " << ((char)('A'+i));
						//i=n;
					}
					else
					{
						p[i] += 1;
					}						
				}	
			}		
		}
		
		cout << endl;
	}
	return 0;
}