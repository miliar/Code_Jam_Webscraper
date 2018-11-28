#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

int main()
{

	FILE *in=fopen("S:/input.in.txt","r");
    FILE *out=fopen("S:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
	
    for (int ii=0;ii < T ;ii++)
    {
		long long r = 0;
		long long t = 0;
		long long cnt=0;
		fscanf(in,"%d %d",&r, &t);
		
		for (long long i=r+1;t>0; i=i+2)
		{
			long long needed = (i*i)-((i-1)*(i-1));
			if ( t >= needed )
			{
				cnt++;
				t=t-needed;
			}
			else
			{
				break;
			}
		}
		fprintf(out,"Case #%d: %d\n",ii+1,cnt);
	}
	return 0;
}