//
//  main.cpp
//  hackercup
//
//  Created by L on 15-1-10.
//  Copyright (c) 2015Äê L. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <queue>
using namespace std;

int main(int argc, const char * argv[]) {
    int T,cas = 1;
    string str;
    int S;
    freopen("C:\\Users\\L\\Downloads\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\A-small-attempt0.out","w",stdout);
    //scanf("%d",&T);
    cin>>T;
    while(T--)
    {
        cout<<"Case #"<<cas++<<": ";
        //scanf("%d",&S);
        //scanf("%d",&str.c_str());
        cin>>S>>str;
        int tol = 0,ans = 0;
        for(int i=0;i<=S;i++)
        {
            int inum = str[i]-'0';
            if(tol < i)
            {
                ans += i-tol;
                tol = i;
            }
            tol += inum;
        }
        cout<<ans<<endl;

    }

    return 0;
}
