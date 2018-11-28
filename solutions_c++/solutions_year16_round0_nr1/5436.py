//
//  main.cpp
//  code_jam_1
//
//  Created by divya gupta on 09/04/16.
//  Copyright (c) 2016 divya gupta. All rights reserved.
//

#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    int t,i;
    cin>>t;
    int x=1;
    while(t--)
    {
        int n,N;
        cin>>N;
        n=N;
        int mark[14]={0};
        if(n==0)
        {
            cout<<"Case #"<<x<<": INSOMNIA"<<endl;
            continue;
        }
        while(1)
        {
            int flag=0;
            int a=n;
            while(a>0)
            {
                mark[a%10]=1;
                a=a/10;
            }
            for(i=0;i<=9;i++)
            {
                if(mark[i]==0)
                    flag=1;
            }
            if(flag==0)
            {
                cout<<"Case #"<<x<<": "<<n<<endl;
                break;
            }
            n+=N;
        }
        x++;
    }
    return 0;
}