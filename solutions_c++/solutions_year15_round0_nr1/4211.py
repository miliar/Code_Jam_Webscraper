//
//  main.cpp
//  codejam1
//
//  Created by Vatsal Chanana on 11/04/15.
//  Copyright (c) 2015 VC. All rights reserved.
//

#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<string>
#include<cstdlib>

using namespace std;


int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int l;
        string s;
        cin>>l>>s;
        l++;
        int init_count=s[0]-'0';
        int added=0;
        
        for(int i=1;i<l;i++)
        {
            if(s[i]=='0')
            {
                continue;
            }
            if(init_count>=i)
            {
                init_count+=s[i]-'0';
                continue;
            }
            else
            {
                added+=(i-init_count);
                init_count=i;
                init_count+=s[i]-'0';
            }
        }
        cout<<"Case #"<<i+1<<": "<<added<<endl;
        
    }
}
