//
//  main.cpp
//  leetcode_cpp
//
//  Created by Xingying Liu on 4/5/16.
//  Copyright © 2016 Xingying Liu. All rights reserved.
//

# include <iostream>
# include <vector>
# include <math.h>

using namespace std;


int cake(string input) {
    int count = 0;
    for (int i=1; i<input.size(); i++)
        if (input[i]!=input[i-1])
            count++;
    if (input.back()=='-')
        count++;
    return count;
}

long long getDiv(long long n){
    for(long long i=2; i*i<=n; i++)
        if(n%i==0) return i;
    return -1;
}

bool checkCand(int cand) {
    vector<long long> result(11, 0);
    vector<long long> scale(11, 1);
    int cur = cand;
    while (cur) {
        for (int base = 2; base<=10; base++) {
            result[base]+=(cur&1)*scale[base];
            scale[base]*=base;
        }
        cur = cur>>1;
    }
    vector <long long> divisor;
    for (int base = 2; base<=10; base++) {
        long long div = getDiv(result[base]);
        if (div == -1)
            break;
        else
            divisor.push_back(div);
    }
    if (divisor.size()==9) {
        cout<<result[10]<<" ";
        for (auto div:divisor) cout<<div<<" ";
        cout<<endl;
        return true;
    }
    else
        return false;
}

void coinJam(int N, int J) {
    int lowerBould = pow(2, N-1) + 1;
    int upperBound = pow(2, N);
    int count = 0;
    
    for (int cand = lowerBould; cand<upperBound && count<J; cand+=2) {
        if (checkCand(cand))
            count++;
    }
}

int main(){
    int T, id = 1;
    cin>>T;
    int N, J;
    while (T--) {
        cout<<"Case #"<<id<<":\n";
        id++;
        cin>>N>>J;
        coinJam(N,J);
    }
    //cout<<"hello world"<<endl;
    return 0;
}