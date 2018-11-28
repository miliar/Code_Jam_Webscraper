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

void printA(LL a)
{
	printf("PPP==> %I64d\n",a);
}

int main(int argc, char** argv)
{
	
	int numTestCase = 0;
	LL rowNum1 =0, rowNum2 = 0, tmpVar = 0;
	VEC row1,row2;
	scanf("%d",&numTestCase);	
	for(int idx=0; idx < numTestCase; ++idx)
	{	
	    row1.clear();
	    row2.clear();
		scanf("%I64d",&rowNum1);
		for(int idy = 0; idy < 4; ++idy)
		{
			for(int idz = 0; idz < 4; ++idz)
			{
			    scanf("%I64d",&tmpVar);		
			    if(idy == rowNum1 - 1)
			    {
			        row1.push_back(tmpVar);	
			    }			
		    }
		}
		scanf("%I64d",&rowNum2);
		for(int idy = 0; idy < 4; ++idy)
		{
			for(int idz = 0; idz < 4; ++idz)
			{
			    scanf("%I64d",&tmpVar);		
			    if(idy == rowNum2 - 1)
			    {
			        row2.push_back(tmpVar);	
			    }	
		   }
		}
		std::sort(row1.begin(),row1.end());		
		std::sort(row2.begin(),row2.end());
		VEC myAnd(4,-1);
		std::set_intersection(row1.begin(),row1.end(),row2.begin(),row2.end(),myAnd.begin());
		int cnt = 0;
		for(int idy = 0; idy < 4; ++idy)
		{
			if( myAnd[idy] != -1 )
			    ++cnt;
		}
		
		if( cnt == 1 )
		    printf("Case #%d: %I64d\n", idx+1, myAnd[0]);
		else if( cnt > 1 )    
		    printf("Case #%d: Bad magician!\n", idx+1);
		else 
		    printf("Case #%d: Volunteer cheated!\n", idx+1);    
	}
	return EXIT_SUCCESS;
}
