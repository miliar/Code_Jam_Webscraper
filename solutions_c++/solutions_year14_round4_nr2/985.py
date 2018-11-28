//
//  main.cpp
//  Round 2 2014. Problem B. Up and Down
//
//  Created by kimtaeyang on 2014. 5. 31..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <algorithm>

int n;

int a[1002];
int answer;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T, n;
    int I,i,j,k,l;
    int left, right;
    
    scanf("%d",&T);
    
    for(I=1; I<=T; I++){
        scanf("%d",&n);
        k=1;
        answer=0;
        
        for(i=1;i<=n;i++){
            scanf("%d",&a[i]);
            //if(a[i] >= a[k]) k=i;
        }
        left=1; right=n;
        
        for(i=1;i<=n;i++){
            k=left;
            for(j=left+1 ; j<=right ; j++){
                if(a[j]<a[k]) k=j;
            }
            if(k-left < right-k){
                for(j=k-1;j>=left;j--) a[j+1]=a[j], answer++;
                left++;
            }
            else{
                for(j=k+1;j<=right;j++) a[j-1]=a[j], answer++;
                right--;
            }
        }
        /*
        for(i=1;i<k;i++){
            for(j=1;j<k-1;j++){
                if(a[j]>a[j+1]){
                    l=a[j];
                    a[j]=a[j+1];
                    a[j+1]=l;
                    answer++;
                }
            }
        }
        for(i=k+1;i<=n;i++){
            for(j=k+1;j<=n-1;j++){
                if(a[j]<a[j+1]){
                    l=a[j];
                    a[j]=a[j+1];
                    a[j+1]=l;
                    answer++;
                }
            }
        }*/
        printf("Case #%d: %d\n",I,answer);
        
    }
    return 0;
    
    
    
}