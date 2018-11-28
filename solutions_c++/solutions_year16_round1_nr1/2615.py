//
//  main.cpp
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//



#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int cas=0;
    while(n--)
    {
        printf("Case #%d: ",++cas);
        string ret="";
        string s;
        cin>>s;
        for(int i=0;i<s.size();i++)
        {
            string p=ret;
            string q=ret;
            p=p+s[i];
            q=s[i]+q;
            if(p>q)
                ret=p;
            else
                ret=q;
        }
        cout<<ret<<endl;
    }
}