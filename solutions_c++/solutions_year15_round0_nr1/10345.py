#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <algorithm>
#include <limits.h>
//#include <functional>
#include <map>
#include <utility> 
//#include <set>
//#include <iostream>
//#include <math.h>


typedef long long LL;
typedef std::vector<LL> VEC;

typedef std::pair<int,int> PII; // accum , needed friend

PII solve(int shyLevel, unsigned long audStr, unsigned long div)
{
    if (shyLevel != 0)
    {
        PII prev = solve(shyLevel-1, audStr / 10,div*10);
        if ( prev.first < shyLevel ) 
        {
            prev.second += shyLevel - prev.first;
            prev.first += shyLevel - prev.first;
        }
        prev.first += audStr % 10  ;        
        return prev; 
    }
    else
    {
        return std::make_pair(audStr,0);
    }
}
int main(int argc, char** argv)
{
	
	int numTestCase = 0;
	int shyMax = 0; 
	unsigned long audStr = 0; 
	scanf("%d",&numTestCase);	
	for(int idx=0; idx < numTestCase; ++idx)
	{	
	    scanf("%d",&shyMax);
		scanf("%ld",&audStr);
        PII ans = solve(shyMax, audStr, 1);
        printf("Case #%d: %d\n", idx + 1, ans.second);
	}
	return EXIT_SUCCESS;
}
