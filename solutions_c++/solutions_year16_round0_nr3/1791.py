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
#define maxn 10005
int main()
{
    
    freopen("/Users/apple/Desktop/in.txt","r",stdin);
    freopen("/Users/apple/Desktop/out.txt","w",stdout);
    int N,J;
    int t;
    scanf("%d",&t);
    int x[100];
    int ans[10];
    int cas=1;
    while(t--){
        printf("Case #%d:\n",cas++);
        scanf("%d%d",&N,&J);
        memset(x,0,sizeof(x));
        x[N-1]=1; x[0]=1;
        while(1){
            int i=1;
            x[i]++;
            while(x[i]>=2){x[i]=0;x[i+1]++;i++;}
            int num=0;
            for(int i=2;i<=10;i++){
                int mark=0;
                for(int j=2;j<200;j++){
                    int tem=1;
                    int sum=0;
                    for(int k=0;k<N;k++){
                        if(x[k]) sum=(sum+tem)%j;
                        tem=(tem*i)%j;
                    }
                    if(sum==0){
                        ans[i]=j;
                        mark=1;
                        break;
                    }
                }
                if(mark) num++;
            }
            if(num==9){
                for(int i=N-1;i>=0;i--) printf("%d",x[i]);
                for(int i=2;i<=10;i++) printf(" %d",ans[i]);
                puts("");
                J--;
            }
            if(J==0) break;
        }
    }
    
}