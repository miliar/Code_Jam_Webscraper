//
//  main.cpp
//  gcj
//
//  Created by Jinfu Leng on 4/11/14.
//  Copyright (c) 2014 jinfu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double A[1005],B[1005];
int N;

void Fun1(){
    int left=0;
    int cnt=0;
    for(int i=0;i<N;i++){
        if(A[i]>B[left]){
            cnt++;
            left++;
        }
    }
    printf("%d ",cnt);
}

void Fun2(){
    //bool used[1005];
    //memset(used,0,sizeof(used));
    int left=0;
    B[N]=1.0;
    for(int i=0;i<N;i++){
        while(B[left]<A[i]) left++;
        if(left==N){
            printf("%d",N-i);
            return;
        }
        else
            left++;
    }
    printf("0");
}

void Fun(){
    Fun1();
    Fun2();
    printf("\n");
}
int main(int argc, const char * argv[])
{
    freopen("/Users/jinfu/Workspace/test/input.in","r",stdin);
    freopen("/Users/jinfu/Workspace/test/output","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        printf("Case #%d: ",t+1);
        scanf("%d",&N);
        for(int i=0;i<N;i++) scanf("%lf",&A[i]);
        sort(A,A+N);
        for(int i=0;i<N;i++) scanf("%lf",&B[i]);
        sort(B,B+N);
        Fun();
    }
    return 0;
}

