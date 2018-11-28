//
//  main.cpp
//  GCJ2016R13B
//
//  Created by Ningchen Ying on 5/8/16.
//  Copyright (c) 2016 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int a[10][10];
int b[60];
int dp[10][10][100];

int main(int argc, const char * argv[]) {
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016R13B/GCJ2016R13B/B-small-attempt1.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016R13B/GCJ2016R13B/B-small-attempt1.out","w",stdout);
    cin>>T;
    for(int icase = 1;icase<=T;icase++){
        int N,M;
        cin>>N>>M;
        int ub = 0;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                a[i][j] = 0;
            }
            //if(i!=N-1) a[i][N-1]=1;
        }
        for(int i=0;i<N-1;i++){
            if(i==0)b[i]=1;
            else b[i]=0;
            for(int j=0;j<N-1;j++){
                if(j>i) a[i][j] = 1;
                if(j<i)b[i]+=b[j];
            }
            //if(i==N-2) b[i]=0;
            //cout<<i<<" "<<b[i]<<endl;
            ub+=b[i];
        }
        //cout<<ub<<endl;
        printf("Case #%d: ",icase);
        if(M>ub){
            printf("IMPOSSIBLE\n");
        }else{
            printf("POSSIBLE\n");
            
            int MM = M;
            
            if(MM==ub){
                for(int i=0;i<N-1;i++){
                    a[i][N-1]=1;
                }
                MM = 0;
            }else{
                int c = 1;
                while(MM){
                    int KK = MM%2;
                    if(KK) a[c][N-1]=1;
                    MM/=2;
                    c++;
                }
            }
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    printf("%d",a[i][j]);
                }printf("\n");
            }
            if(MM!=0) while(1);
        }
    }
    return 0;
}
