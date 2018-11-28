//
//  main.cpp
//  codejam
//
//  Created by Apple on 16/4/9.
//  Copyright © 2016年 Apple. All rights reserved.
//

#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    
    freopen("/Users/apple/Desktop/in.txt","r",stdin);
    freopen("/Users/apple/Desktop/out.txt","w",stdout);
    scanf("%d",&t);
    int cas=1;
    while(t--){
        int n;
        scanf("%d",&n);
        int x[10];
        int num=0;
        int ans=-1;
        memset(x,0,sizeof(x));
        for(int i=1;i<6000;i++){
            int tem=i*n;
           // printf("%d\n",tem);
            while(tem>0){
                int u=tem%10;
                if(x[u]==0){
                    x[u]++;
                    num++;
                }
                tem/=10;
            }
            if(num==10){
                ans=i*n;
                break;
            }
        }
        printf("Case #%d: ",cas++);
        if(ans==-1) puts("INSOMNIA");
        else printf("%d\n",ans);
    }
}