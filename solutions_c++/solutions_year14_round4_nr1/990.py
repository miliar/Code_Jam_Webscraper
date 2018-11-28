//
//  main.cpp
//  Round 2 2014. Problem A. Data Packing
//
//  Created by kimtaeyang on 2014. 5. 31..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <algorithm>

int n, size;
int a[800];
int answer;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T;
    int I,i,j;
    
    scanf("%d",&T);
    
    for(I=1; I<=T; I++){
        answer=0;
        scanf("%d%d",&n,&size);
        
        for(i=0;i<=700;i++) a[i]=0;
        for(i=1;i<=n;i++) scanf("%d",&j), a[j]++;
        
        for(i=700;i>=1;i--) if(a[i]>0){
            if(i+i<=size){
                for(j=i-1;j>=0;j--) a[j]+=a[j+1];
                answer+=(a[0]+1)/2;
                break;
            }
            for(j=size-i;j>=1;j--){
                if(a[j]<a[i]){
                    answer+=a[j];
                    a[i]-=a[j];
                    a[j]=0;
                }
                else {
                    answer+=a[i];
                    a[j]-=a[i];
                    a[i]=0;
                    break;
                }
            }
            answer+=a[i];
        }
        printf("Case #%d: %d\n",I,answer);
    }
    
    return 0;
    
}

