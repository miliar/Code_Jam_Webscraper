//
//  main.cpp
//  Codejam2013
//
//  Created by hams on 13. 4. 13..
//  Copyright (c) 2013년 hams. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <math.h>


bool isPD(long long value){
    char buffer[1024] = {0,};
    sprintf(buffer,"%lld",value);
    long strn = strlen(buffer);
    //long half = (long)((strn/2.0)+0.5);
    //printf("input:%s,size:%ld,half:%d\n",buffer,strn,half);
    long ni=0;long nj=0;
    for(ni=0,nj=strn-1; ni <= strn/2 ; ++ni, --nj){
        //printf("[%02d]f:%c,b:%c\n",ni,buffer[ni],buffer[nj]);
        if(buffer[ni] != buffer[nj])
            return false;
    }
    
    return true;
}

bool isSQ( double value){
    //printf("value:%f\n",value);
    return (sqrt(value) - (long)sqrt(value) == 0) ? true:false;
//    double sq = sqrt(value) - (long)sqrt(value);
//    //printf("sqrt:%f,(long)sqrt:%ld\n",sqrt(value),(long)sqrt(value));
//    //printf("sq:%f\n",sq);
//    if( sq != 0)
//        return false;
//    return true;
}


int main()
{
    int T =0;
    scanf("%d",&T);
    //printf("%d\n",isSQ(10000000*(double)10000000));
    
    long long A=0,B=0;
    for(int nloop=0; nloop < T; ++nloop){
        scanf("%lld",&A);
        scanf("%lld",&B);
		long long sA = (long long)sqrt(A);
		long long sB = (long long)sqrt(B);
        
        long count = 0;
	
        for(long long ni=sA; ni <= sB; ++ni){
			//if(ni%10000000 == 0) printf("ni:%lld\n",ni);
            if(isPD(ni)){
                //if(isSQ(ni) && isPD(ni*ni))// && isPD(sqrt(ni)))
                if(isPD(ni*ni))
			if(ni*ni >= A && ni*ni <= B)
				count++;
            }
        }
        printf("Case #%d: %ld\n",nloop+1,count);
    }
    
    
}
