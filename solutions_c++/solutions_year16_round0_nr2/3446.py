//
//  main.cpp
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
string s;
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        cin>>s;
        int ans=0;
        for(int i=(int)s.size();i>=0;i--)
        if(s[i]=='-')
        {
            if(s[0]=='+')
            {
                int j=0;
                while(s[j]=='+')
                {
                    s[j]='-';
                    j++;
                }
                ans++;
            }
            string t=s.substr(i+1);
            string v=s.substr(0,i+1);
            reverse(v.begin(),v.end());
            for(int i=0;i<v.size();i++)
            {
                if(v[i]=='+')
                    v[i]='-';
                else
                    v[i]='+';
            }
            s=v+t;
            ans++;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}