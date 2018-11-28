//
//  main.cpp
//  CookieClickerAlpha
//
//  Created by Yitao Liang on 14-4-11.
//  Copyright (c) 2014年 Yitao Liang. All rights reserved.
//

#include <iostream>
using namespace std;

int main(){
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt","w",stdout);
    int t;
    double c,f,x,p,timeNeeded,s,t2;
    t2=0.0;
    timeNeeded=0.0;
    cin>>t;
    for (int i=1;i<=t;i++){
        cin>>c;cin>>f;cin>>x;
        p=2.0;
        s=0.0;
        while (true){
            timeNeeded=(float)x/p;
            t2=(c/p)+x/(p+f);
            if (timeNeeded<=t2){
                timeNeeded+=s;
                printf("Case #%d: %.7f\n",i,timeNeeded);
                break;
            }else{
                s+=c/p;
                p+=f;
            }
        }
    }
    return 0;
}