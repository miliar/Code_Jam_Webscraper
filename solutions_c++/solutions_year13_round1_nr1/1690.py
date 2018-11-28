//
//  main.cpp
//  google code jam
//
//  Created by Navid on 4/26/13.
//  Copyright (c) 2013 Navid. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[])
{
    
	int T,C=1;
	int t,area;
	int r,result;
	scanf("%d",&T);

	while(T--)
	{
		scanf("%d %d",&r,&t);
        result=0;
        area=(2*r)+1;
        while(t>=area)
        {
            t-=area;
            r+=2;
            area=(2*r)+1;
            result++;
        }
		printf("Case #%d: %d\n",C++,result);
        
        
    
	}
	return 0;

}

