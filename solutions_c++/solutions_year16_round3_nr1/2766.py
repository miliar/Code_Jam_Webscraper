//
//  main.cpp
//  problem1
//
//  Created by zjl on 16/5/8.
//  Copyright © 2016年 zjl. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
using namespace std;


int party[26];
int sum;
int T, N, t;

int largest(){
    int idx=0, maxp=0;
    for(int i=0;i<N;i++){
        if(party[i]>maxp){
            maxp = party[i];
            idx = i;
        }
    }
    party[idx]--;
    sum--;
    return idx;
}

void res(){
   

}

int main(int argc, const char * argv[]) {
    freopen("/Users/zjl/Documents/google/problem1/problem1/A-large.in","r",stdin);
    freopen("/Users/zjl/Documents/google/problem1/problem1/test_out2.txt","w",stdout);
    cin>>T;
    for(int j=1; j<=T; j++){
        sum = 0;
        cin>>N;
        for(int i=0;i<N;i++){
            cin>>party[i];
            sum += party[i];
        }
        cout<<"Case #"<<j<<": ";
        while(sum>3){
            
            t = largest();
            cout<<(char)('A'+t);
            t = largest();
            cout<<(char)('A'+ t)<<" ";
        }
        if(sum==3){
            t = largest();
            cout<<(char)('A'+t)<<" ";
        }
        t = largest();
        cout<<(char)('A'+t);
        t = largest();
        cout<<(char)('A'+t)<<endl;
    }

    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
