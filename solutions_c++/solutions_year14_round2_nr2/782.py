//
//  main.cpp
//  Round 1B 2014. problem B
//
//  Created by kimtaeyang on 2014. 5. 4..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T;
    
    int i,j;
    
    int a,b,k;
    
    scanf("%d",&T);
    
    int count;
    
    for(int I=1;I<=T;I++){
        
        scanf("%d%d%d",&a,&b,&k);

        count=0;
        
        for(i=0;i<a;i++) for(j=0;j<b;j++) if((i&j)<k) count++;
        
        printf("Case #%d: %d\n",I,count);
    }
    
}
