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
int p[1010];

int main(int argc, const char * argv[]) {
    int T,cas = 1;
    string str;
    int D,maxp;
    freopen("C:\\Users\\L\\Downloads\\B-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\B-small-attempt0.out","w",stdout);
    cin>>T;
    while(T--)
    {
        int ans;
        maxp = -1;
        cout<<"Case #"<<cas++<<": ";
        cin>>D;
        for(int i=0;i<D;i++){
            cin>>p[i];
            maxp = max(maxp,p[i]);
        }
        ans = maxp;
        for(int i=1;i<=maxp;i++)
        {
            int tmpans = 0;
            for(int j=0;j<D;j++)
            {
                if(p[j]>i)
                {
                    tmpans += (p[j]+(i-1))/i - 1;
                }
            }
            tmpans += i;
            ans = min(tmpans,ans);
        }
        cout<<ans<<endl;
    }

    return 0;
}
