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
struct xu{
    int index;
    int time;
}x[1005];

bool comp(struct xu a, struct xu b)
{
    if(a.time < b.time)
        return true;
    else if(a.time == b.time && a.index > b.index)
        return true;
    else
        return false;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Fannn/Downloads/B-Large.in.txt","r",stdin);
    freopen("/Users/Fannn/Downloads/B-Large.out.txt","w",stdout);
    int T,cas=1,n,B;
    long long int a[1005];
    cin>>T;
    while(T--)
    {
        cin>>B>>n;
        for(int i=0;i<B;i++)
            cin>>a[i];
        long long int fck = 1;
        long long int  start = 0,end = (long long int )n * (long long int)a[0];
        long long int all;
        while(start < end)
        {
            long long int mid = (start + end)/2;
            all=0;
            for(int i=0;i<B;i++)
                all+= (mid+a[i]-1) / a[i];
          //  if(all < 0)
          //      cout<<"hehe"<<endl;
            if(all>=n)
                end = mid;
            else
                start = mid+1;
        }
        
        all=0;
        for(int i=0;i<B;i++)
            all+= (end+a[i]-1) / a[i];
        long long int cha = all - n;
        //if(cha >=5 )
        //    cout<<"hehe"<<endl;
        for(int i=0;i<B;i++){
            x[i].index = i;
            x[i].time = (end-1+a[i]) % a[i];
        }
        
        sort(x,x+B,comp);
        
        cout<<"Case #"<<cas++<<": ";
        cout<<x[cha].index + 1<<endl;
    }
    

    return 0;
}