//
//  main.cpp
//  GCJQA
//
//  Created by Ningchen Ying on 4/12/14.
//  Copyright (c) 2014 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main(int argc, const char * argv[])
{
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/GCJQA/GCJQA/A-small-attempt0.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJQA/GCJQA/A-small-attempt0.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        int a,b;
        cin>>a;
        map<int,int> ync;
        ync.clear();
        
        for(int i=1;i<=4;i++){
            for(int j=0;j<4;j++){
                cin>>b;
                if(i==a) ync[b]=1;
            }
        }
        
        cin>>a;
        int cn=0;
        int ans=0;
        for(int i=1;i<=4;i++){
            for(int j=0;j<4;j++){
                cin>>b;
                if(i==a && ync[b]==1){
                    ans=b;
                    cn++;
                }
            }
        }
        cout<<"Case #"<<cas<<": ";
        if(cn==0) cout<<"Volunteer cheated!"<<endl;
        if(cn==1) cout<<ans<<endl;
        if(cn>1) cout<<"Bad magician!"<<endl;
    }
    return 0;
}

