#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

int main (int argc, char const* argv[])
{
	int test, fr, sr, tmp, tot;
	int cs[17];
	cin>>test;
	for (int i = 1; i <= test; i += 1)
	{
	        memset(cs,0,sizeof(cs));
		cin>>fr;
		for (int j = 0; j < 4; j += 1)
		{
			for (int k = 0; k < 4; k += 1)
			{
				cin>>tmp;
				if (j+1==fr)
				{
					cs[tmp] += 1;
				}
			}
		}
		cin>>sr;
		for (int j = 0; j < 4; j += 1)
		{
			for (int k = 0; k < 4; k += 1)
			{
				cin>>tmp;
				if (j+1==sr)
				{
					cs[tmp] += 1;
				}
			}
		}
		tot = 0;
		for (int j = 0; j < 17; j += 1)
		{
			if (cs[j]==2)
			{
				tot += 1;
				tmp = j;
			}
		}
		if (tot==0)
		{
			printf("Case #%d: Volunteer cheated!\n",i);
		}
		else if (tot==1)
		{
			printf("Case #%d: %d\n",i,tmp);
		}
		else printf("Case #%d: Bad magician!\n",i);
	}
	return 0;
}





