//
//  main.cpp
//  Repeater
//
//  Created by Minghui Liu on 5/3/14.
//  Copyright (c) 2014 Minghui Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

typedef vector<string> vs;
typedef vector<vector<int>> vvi;

int helperFunc(int a, int b){
    if(a<b){
        return b-a;
    }else{
        return a-b;
    }
}

int findRes(vs & coreString,vvi & countTotal, int N){
    int j;
    string coreStringModel=coreString[0];
    for(j=1;j<N;j++){
        if(coreString[j]!=coreStringModel){
            return -1;
        }
    }
    int diffChar = (int)(coreString[0].size());
    int res = 0;
    for(j=0;j<diffChar;j++){
        int k;
        double sum=0.0;
        for(k=0;k<N;k++){
            sum+=countTotal[k][j];
        }
        double avg = sum/N;
        int avgInt = sum/N;
        if(avg-avgInt>0.5){
            avgInt+=1;
        }
        for(k=0;k<N;k++){
            res+=helperFunc(countTotal[k][j],avgInt);
        }
    }
    return res;
}

void solve(int i, int N, vs & original){
    int j;
    vector<string> coreString(N);
    vector<vector<int>> countTotal(N,vector<int>(100));
    for(j=0;j<N;j++){
        coreString[j].push_back(original[j][0]);
        int k;
        int stringLen = (int)(original[j].size());
        int count = 0;
        countTotal[j][count]=1;
        for(k=1;k<stringLen;k++){
            if(original[j][k]==coreString[j][count]){
                countTotal[j][count]++;
            }else{
                count++;
                coreString[j].push_back(original[j][k]);
                countTotal[j][count]++;
            }
        }
    }
    int result;
    result = findRes(coreString,countTotal,N);
    if(result==-1){
        cout<<"Case #"<<i+1<<": Fegla Won"<<endl;
    }else{
        cout << "Case #"<<i+1<<": "<<result<<endl;
    }
}


int main(int argc, const char * argv[])
{
    freopen("/Users/minghui/Documents/C++/Repeater/Repeater/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/minghui/Documents/C++/Repeater/Repeater/A-small-attempt0.out.txt", "w", stdout);
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++){
        int N;
        cin >> N;
        vector<string> original;
        int j;
        for(j=0;j<N;j++){
            string tmp;
            cin >> tmp;
            original.push_back(tmp);
        }
        solve(i,N,original);
    }
    
    return 0;
}

