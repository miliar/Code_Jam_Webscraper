//
//  main.cpp
//  Standing Ovation
//
//  Created by Dhruv Mullick on 11/04/15.
//  Copyright (c) 2015 Dhruv Mullick. All rights reserved.
//

#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define f first
#define s second
typedef pair<int,int> ii;
typedef pair<int,pair<int,int> > iii;

int main(int argc, const char * argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t,sum,c,i,n,smax;
    string S;
    
    freopen("A.txt","r",stdin);
    
    cin>>t;
    
    for(int j=1;j<=t;j++)
    {
        cin>>smax;
        cin>>S;
        c=0;
        sum=0;
        
        for(i=0;i<S.size();i++)
        {
            if(i==0)
            {
                sum=S[i]-'0';
                continue;
            }
            
            n = i;
            
            if(sum>=n)
                sum=sum+(S[i]-'0');
            else
            {
                c+=n-sum;
                sum=n+(S[i]-'0');
            }
            
        }
        
        cout<<"Case #"<<j<<": "<<c<<"\n";
        
    }
    
    return 0;
}
