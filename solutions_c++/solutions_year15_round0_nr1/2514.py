//
//  main.cpp
//  q1
//
//  Created by Arvind on 11/04/15.
//  Copyright (c) 2015 NSIT. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string per;
long int smax;

long long int solve(){
    
    long long int standing=0,reqd=0,i=0;
    while(i<=smax){
        if(standing>=i){
            standing+=per[i];
            i++;
        }
        else{
            reqd+=i-standing;
            standing=i;
        }
    }
    return reqd;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int it=1;it<=t;it++){
        cin>>smax;
        cin>>per;
        for(int i=0;i<=smax;i++)
            per[i]=per[i]-'0';
        cout<<"Case #"<<it<<": "<<solve()<<endl;
        
    }
    
    return 0;
}