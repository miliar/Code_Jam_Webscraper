//
//  main.cpp
//  GCJ2016
//
//  Created by Ningchen Ying on 4/9/16.
//  Copyright (c) 2016 Ningchen Ying. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int a[1000100];
    for(int i=0;i<=1000000;i++){
        int b[10];
        for(int j=0;j<10;j++){
            b[j]=0;
        }
        a[i] = -1;
        int x = i;
        int res = 0;
        for(int j=1;j<=2000;j++){
            int y = x*j;
            while(y){
                int p = y%10;
                y/=10;
                if (b[p] == 0){
                    res++;
                    b[p]=1;
                }
            }
            if(res==10){
                a[i]=x*j;
                //cout<<i<<" "<<a[i]<<endl;
                break;
            }
        }
    }
    int T,N;
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/A-large.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/A-large.out","w",stdout);
    cin>>T;
    
    for(int icase = 1;icase<=T;icase++){
        cin>>N;
        if(a[N]==-1){
            printf("Case #%d: INSOMNIA\n",icase);
        }else{
            printf("Case #%d: %d\n",icase,a[N]);
        }
    }
    
    return 0;
}
