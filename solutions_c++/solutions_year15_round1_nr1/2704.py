//
//  main.cpp
//  q1
//
//  Created by Arvind on 18/04/15.
//  Copyright (c) 2015 NSIT. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

int n;
long long int sum;
int m[1005];
int drops[1005];

void initialize(){
    for(int i=0;i<1005;i++){
        m[i]=0;
        drops[i]=0;
    }
}
inline int maxi(int a,int b)
{ return a>b?a:b; }
inline int mini(int a,int b)
{ return a<b?a:b; }

void solve(){
    int ld=0;
    
    drops[0]=0;
    sum =0;
    for(int i=1;i<n;i++)
    {
        drops[i]=maxi(0,m[i-1]-m[i]);
        sum+=drops[i];
        ld=maxi(ld,drops[i]);
    }
    cout<<sum<<" ";
    //temp=ld/(double)10;
   // speed = ld;
    sum=0;
    for(int i=0;i<n-1;i++){
        sum+=mini(ld,m[i]);
    }
    cout<<sum<<endl;
}


int main(int argc, const char * argv[]) {
    
    freopen("inp.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int it=1;it<=t;it++){
        initialize();
        cin>>n;
        for(int i =0;i<n;i++)
            cin>>m[i];
        cout<<"Case #"<<it<<": ";
        solve();
    }

    return 0;
}
