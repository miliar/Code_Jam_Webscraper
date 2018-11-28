//
//  main.cpp
//  GCJ2016
//
//  Created by Ningchen Ying on 4/9/16.
//  Copyright (c) 2016 Ningchen Ying. All rights reserved.
//

#include <stdio.h>
#include <limits.h>
#include <vector>
#include <math.h>
#include <iostream>
#include "time.h"
#include <bitset>
#include <fstream>
using namespace std;

int test(long long y){
    int h = (int)(sqrt(y));
    for(int i=2;i<=h;i++){
        if(y%i==0) return i;
    }
    return -1;
}

int main(int argc, const char * argv[]) {
    
    int T;
    
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/C-small-attempt1.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/C-small-attempt1.out","w",stdout);
    cin>>T;
    for(int icase = 1;icase<=T;icase++){
        int N,J;
        cin>>N>>J;
        int l = 1<<(N-1);
        int r = 1<<N;
        
        int id = 0;
        printf("Case #%d:\n",icase);
        for(int i=l;i<r;i++){
            int x = i;
            if(x%2==0) continue;
            bool f = true;
            int a[20];
            for(int j=0;j<=10;j++) a[j]=-1;
            for(int j=2;j<=10 && f;j++){
                int q=x;
                long long y=0;
                while(q){
                    int d = q%2;
                    y = y*(long long)j+(long long)d;
                    q/=2;
                }
                //cout<<j<<" "<<y<<endl;
                int res = test(y);
                if(res==-1){
                    f = false;
                }else{
                    a[j]=res;
                }
            }
            if(f){
                id++;
                long long y=0;
                int q = i;
                while(q){
                    int d = q%2;
                    y = y*(long long)10+(long long)d;
                    q/=2;
                }
                cout<<y;
                for(int j=2;j<=10;j++) cout<<" "<<a[j];
                cout<<endl;
            }
            if(id==J) break;
        }
        
        //cout<<res<<endl;
    }
    

    return 0;
}
