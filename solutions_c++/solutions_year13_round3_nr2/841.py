#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	
	int t,cc=1;
	scanf ("%d",&t);

	while (t--)
	{
		int x,y;
		scanf ("%d %d",&x,&y);

		string ret;

		if (abs (x)<abs(y))
		{
			char s;
			if (y<0)
				s = 'S';
			else
				s = 'N';
			int cy = 0;
			int c = 0;
			while (y!=cy)
			{
				//cout << cy << " " << c << endl;
				c++;
				if (c==abs(x))
				{
					if (x<0)
						ret += 'W';
					else
						ret += 'E';
					
					if (cy<y)
					{
						if (cy+1+c>y)
							s = 'S';
						else
							s = 'N';
					}
					else
					{
						if (cy-c-1<y)
							s = 'N';
						else
							s = 'S';
					}
					continue;
				}
				ret+=s;
				cy += (s=='S'?-1:1)*c;
				s = s=='S'?'N':'S';
			}
		}
		else
		{
			char s;
			if (x<0)
				s = 'W';
			else
				s = 'E';
			int cx = 0;
			int c = 0;
			while (x!=cx)
			{
				//cout << x << " " << cx << " " << c << endl;
				c++;
				if (c==abs(y))
				{
					if (y<0)
						ret += 'S';
					else
						ret += 'N';
					if (cx<x)
					{
						if (cx+c+1>x)
							s = 'W';
						else
							s = 'E';
					}
					else
					{
						if (cx-c-1<x)
							s = 'E';
						else
							s = 'W';
					}
					continue;
				}
				ret+=s;
				cx += (s=='W'?-1:1)*c;
				s = s=='W'?'E':'W';
			}
		}
		printf ("Case #%d: %s\n",cc++,ret.c_str());
	}
	
	return 0;
}
