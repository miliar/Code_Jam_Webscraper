#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>
#include <fstream>

using namespace std;

typedef  unsigned int uint;

uint ghi[100];
uint ghinum;
uint gin[100][100];
uint tag[100][100];


uint scan(uint n,uint m,uint height)
{
    uint i,j,x,y;
	uint flag;
	uint hflg,lflg;

	for(i = 0;i < n;i++)
	{
	    for(j = 0;j< m;j++)
    	{
    	    if(height == gin[i][j])
    	    {
    	        hflg = 0;lflg = 0;
    	        //lie;
    	        for(x = 0;x< n;x++)
    	        {
    	            if(height < gin[x][j])
    	            {hflg = 1;}
    	        }
    	        //hang;
    	        for(x = 0;x< m;x++)
    	        {
    	            if(height < gin[i][x])
    	            {lflg = 1;}
    	        }

				if((1 == hflg)&&(1 == lflg))
				{return 1;}
    	    }
    	}
	}

	return 0;
#if 0
	
    flag = 0;
	for(i = 0;i < n;i++)
	{
	    for(j = 0;j< m;j++)
    	{
    	    if(0 == tag[i][j])
	    	{
    	    	if(gin[i][j] == height)
    	    	{
    	    	    flag = 0;
    	    	    // scan colomn;
    	    	    for(x = 0;x < n;x++)
    	    	    {
    	    	        if((gin[x][j] != height)&&(0 == tag[x][j]))
    	    	        {flag = 1;}
    	    	    }
					if(0 == flag)
					{
					    for(x = 0;x < n;x++)
				    	{
					        tag[x][j] = 1; 
					    }
					}
					else
					{

    					flag = 0;
    					// scan row;
    					for(y = 0;y < m;y++)
        	    	    {
        	    	        if((gin[i][y] != height)&&(0 == tag[i][y]))
        	    	        {flag = 1;}
        	    	    }
    					if(0 == flag)
    					{
    					    for(y = 0;y < m;y++)
    				    	{
    					        tag[i][y] = 1; 
    					    }
    					}
					}
    	    	}
	    	}
    	}
	}

	
    return flag;
#endif
}

void main()
{

    uint t,tidx;
	uint n,m;
	uint i,j,k;
	uint tmp;
	uint re,flag;
	fstream testfin,testfout;

    testfout.open("out.txt",ios::out);
	testfin.open("B-large.in",ios::in);

    testfin >> t;


	/////////////////////////////
	for(tidx = 1;tidx < (t+1);tidx++)
	{

        testfin >>n;
		testfin >>m;

		for(i = 0; i < n;i++)
    	{
    	    for(j = 0; j < m;j++)
    	    {
    	        testfin >>gin[i][j];
	    	}
		}
	
    	flag= 0;
    	re = 0;
        ghinum = 0;
    	tmp = 0;



		
    
        ghi[0] = gin[0][0];
    	ghinum++;
    
    
    	//  get height;
    	for(i = 0; i < n;i++)
    	{
    	    for(j = 0; j < m;j++)
    	    {
    	        
    	        tag[i][j] = 0;
    			flag = 0;
    		    for(k = 0; k < ghinum;k++)
    	        {
    	            if(gin[i][j] == ghi[k])
    	            {
    	                flag =1;
    	                
    	            }
    	        }
    
    			if(0 == flag)
    			{
    			    ghi[ghinum] = gin[i][j];
                    ghinum++;
    			}
    			
    	        	
    	    }
    	}

		if(1 == ghinum)
		{
		    testfout << "Case #" << tidx << ": YES"  << endl;
		    continue;
		}
    
    
    	//sort;
    	for(i = 0;i < (ghinum-1);i++)
    	{
    	    for(j = i+1;j<ghinum;j++)
    	    {
    	        if(ghi[j] < ghi[i])
    	        {
    	            tmp = ghi[i];
    				ghi[i] = ghi[j];
    				ghi[j] = tmp;
    	        }
    	    }
    	}
    
    	//scan  and reduce;
    
    	for(k = 0; k < ghinum;k++)
    	{
    	    re += scan(n,m,ghi[k]);
    	}
		
 
		
        if(0 == re)
    	{
 
		    testfout << "Case #" << tidx << ": YES"  << endl;
    	}
		else
		{
		    testfout << "Case #" << tidx << ": NO"  << endl;
		}
	}

}