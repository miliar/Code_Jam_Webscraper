//
//  main.cpp
//  CodeJam15P
//
//  Created by Ningchen Ying on 4/11/15.
//  Copyright (c) 2015 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int p[1005];
int dp[1005][1005];
int main(int argc, const char * argv[]) {
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/CodeJam15P/CodeJam15P/B-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/CodeJam15P/CodeJam15P/B-large.out","w",stdout);
    dp[0][0]=0;
    for(int i=0;i<=1000;i++){
        for(int j=0;j<=1000;j++){
            if(j>=i){
                dp[i][j]=0;
                continue;
            }
            if(i!=0 && j ==0){
                dp[i][j] = 10000;
                continue;
            }
            dp[i][j] = dp[i-1][j-1];
            for(int k=1;k<i;k++)
                dp[i][j]=min(dp[k][j]+dp[i-k][j]+1,dp[i][j]);
            //if(dp[i][j]>dp[i][j-1]) cout<<i<<" "<<j<<endl;
        }
        //cout<<i<<endl;
    }
    cin>>T;
    //cout<<T<<endl;
    for(int cas=1;cas<=T;cas++){
        int ans,d;
        cin>>d;
        for(int i=0;i<d;i++) cin>>p[i];
        sort(p,p+d);
        ans = p[d-1];
        int n = p[d-1];
        for(int i=n-1;i>=0;i--){
            int ad = 0;
            for(int j=0;j<d;j++){
                ad+=dp[p[j]][i];
            }
            ans = min(ans,i+ad);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
