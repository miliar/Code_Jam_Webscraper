//
//  main.cpp
//  code_C
//
//  Created by yxfish13 on 15/4/11.
//  Copyright (c) 2015年 x-yu13. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;
int L,X;
char S[20000];
const int multi[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int main(int argc, const char * argv[]) {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int nowdata = 1;nowdata<=T;nowdata++){
        scanf("%d%d\n",&L,&X);
        gets(S);
        int now=1,kt=0;
        for (int i = 0;i < L*X; i++){
            char ch=S[i%L];
            if (ch=='i') ch = 2;
            if (ch=='j') ch = 3;
            if (ch=='k') ch = 4;
            int ts=abs(now);
            ts=multi[ts-1][ch-1];
            if (now<0) now = -ts;else now =ts;
            if (now==2&&kt==0) kt=2;
            if (kt==2&&now==4) kt=4;
        }
        if (kt==4&&now==-1) printf("Case #%d: YES\n",nowdata);
        else printf("Case #%d: NO\n",nowdata);
    }
    return 0;
}
