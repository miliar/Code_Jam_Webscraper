//
//  main.cpp
//  Counting Sheep
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

int C[11];

int main(int argc, const char * argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t,i,j;
    ll n,x,d,k;
    
    freopen("/Users/dhruvmullick/CS/in.txt","r",stdin);
    freopen("/Users/dhruvmullick/CS/out.txt","w",stdout);

    
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        fill(C,C+10,0);
        k=1;
        
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        
        while(1)
        {
            x=n*k;
            
            while(x)
            {
                d=x%10;
                x/=10;
                C[d]++;
            }
            
            for(j=0;j<=9;j++)
                if(C[j]==0)
                    break;
            if(j==10)
                break;
            k++;
        }
        cout<<"Case #"<<i<<": ";
        cout<<n*k<<"\n";
    }
    
    return 0;
}
