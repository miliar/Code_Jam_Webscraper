//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Dhruv Mullick on 09/04/16.
//  Copyright © 2016 Dhruv Mullick. All rights reserved.
//

#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pb push_back
#define f first
#define s second
#define PI 3.14159265359
typedef pair<int,int> ii;
typedef pair<int,pair<int,int> > iii;

int main(int argc, const char * argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t,n,T,i,j;
    int dp[101][2];
    string str;
    
    freopen("/Users/dhruvmullick/CS/in.txt","r",stdin);
    freopen("/Users/dhruvmullick/CS/out.txt","w",stdout);

    cin>>t;
    
    for(T=1;T<=t;T++)
    {
        cin>>str;
        for(i=0;i<=100;i++)
            dp[i][0]=dp[i][1]=0;
        
        if(str[0]=='-')
        {
            dp[0][0]=0;
            dp[0][1]=1;
        }
        else
        {
            dp[0][0]=1;
            dp[0][1]=0;
        }
            
        for(i=1;i<str.size();i++)
        {
            if(str[i]=='-')
            {
                dp[i][0]=dp[i-1][0];
                dp[i][1]=dp[i-1][0]+1;
            }
            else
            {
                dp[i][0]=1+dp[i-1][1];
                dp[i][1]=dp[i-1][1];
            }
        }
        cout<<"Case #"<<T<<": ";
        cout<<dp[str.size()-1][1]<<"\n";
    }
    
    return 0;
}
