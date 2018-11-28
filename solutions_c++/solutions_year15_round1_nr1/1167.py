//
//  main.cpp
//  hackercup
//
//  Created by L on 15-1-10.
//  Copyright (c) 2015年 L. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <queue>
#include <sstream>
using namespace std;


int main(int argc, const char * argv[]) {
    freopen("/Users/Fannn/Downloads/A-large.in.txt","r",stdin);
    freopen("/Users/Fannn/Downloads/A-large.out.txt","w",stdout);
    int T,cas=1,n;
    int a[1005];
    cin>>T;
    int ans1,ans2;
    while(T--)
    {
        //scanf("%d %d %d %d",&n,&m,&a,&b);
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>a[i];
        ans1 = 0;
        ans2 = 0;
        int maxx = 0;
        for(int i=1;i<n;i++)
            if(a[i-1]-a[i] > 0){
                ans1 += a[i-1] - a[i];
                if(a[i-1] - a[i] > maxx)
                    maxx = a[i-1]- a[i];
            }
        for(int i=0;i<n-1;i++)
            if(a[i]<maxx)
                ans2 += a[i];
            else
                ans2 += maxx;
        cout<<"Case #"<<cas++<<": ";
        cout<<ans1<<" "<<ans2<<endl;
    }
    

    return 0;
}