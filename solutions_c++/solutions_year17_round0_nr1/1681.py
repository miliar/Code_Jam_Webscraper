//
//  main.cpp
//  tmp
//
//  Created by 金航宇 on 2017/4/8.
//  Copyright © 2017年 金航宇. All rights reserved.
//

#include <iostream>
#include<cstring>
#define N 2000
using namespace std;

int cas=0,tt;
int k;
string s;
bool x[N];
int main()
{
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    cin>>tt;
    while(tt--)
    {
        cin>>s;
        cin>>k;
        int n=s.length();
        int cnt=0;
        for(int i=1;i<=n;i++)
        {
             x[i]=(s[i-1]=='-')?1:0;
            for(int j=1;j<k&&j<i;j++)x[i]^=x[i-j];
            if(x[i])cnt++;
        }
        //for(int i=1;i<=n;i++)cout<<x[i];
        //cout<<endl;
        cout<<"Case #"<<++cas<<": ";
        bool f=0;
        for(int j=0;j<k-1;j++)if(x[n-j]){f=1;break;}
        if(f)cout<<"IMPOSSIBLE"<<endl;
        else cout<<cnt<<endl;
    }
    return 0;
}
