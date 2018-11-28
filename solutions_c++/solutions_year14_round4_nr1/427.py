//
//  main.cpp
//  GCJ14_R2
//
//  Created by Ningchen Ying on 5/31/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int a[10010];

int main(int argc, const char * argv[])
{
    int T;
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2/GCJ14_R2/A-small-attempt0.in","r",stdin);
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2/GCJ14_R2/A-small-attempt0.out","w", stdout);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2/GCJ14_R2/A-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ14_R2/GCJ14_R2/A-large.out","w", stdout);
    cin>>T;
    
    for(int ca=1;ca<=T;ca++){
        int N,X;
        cin>>N>>X;
        for(int i=0;i<N;i++){
            cin>>a[i];
        }
        sort(a,a+N);
		int st=0;
		int ans=0,i;
		for(i=N-1;i>st;i--){
			if(a[i]+a[st]<=X){
				st++;
			}
			ans++;
		}
		if(i>=st)ans++;
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

