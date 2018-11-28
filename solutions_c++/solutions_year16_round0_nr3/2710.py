//
//  main.cpp
//  CoinJam
//
//  Created by MichelleShieh on 4/9/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

#include <iostream>
#include <map>
#include <cmath>
#include <vector>
using namespace std;

//const long long SAMPLE = 100000000;
//const long long SMALL = 1111111111111111;

//map<long long,bool> prime;

int n,j;

bool isPrime (long long number) {
    bool temp = true;
    for (long long j=2;j<sqrt(number);j=j+1) {
        if (number%j==0) {
            temp = false;
            break;
        }
    }
    if (temp == true) {
        return true;
    }
    else {
        return false;
    }
}

long long getNum(int base,int num[]) {
    long long ans = 0;
    long long times = 1;
    for (int i = n-1; i>=0; i--) {
        ans += num[i] * times;
        times *=base;
    }
    return ans;
}

void check(int num[],int n) {
    long long number;
    if (j<=0) return;
    vector<long long> divisor;
    bool temp = true;
    for (int i=2;i <= 10;i++ ) {
        number = getNum(i,num);
        if (isPrime(number) == true ) {
            temp = false;
            break;
        }
        else {
            for (long long i=2;i<sqrt(number);i++) {
                if (number % i == 0) {
                    divisor.push_back(i);
                    break;
                }
            }
        }
    }
    if (temp == true) {
        j--;
        for (int i = 0; i< n; i++) {
            cout<<num[i];
        }
        for (int i = 0;i < divisor.size(); i++) {
            cout<<" "<<divisor[i];
        }
        cout<<endl;
    }
}

void dfs (int num[], int ptr,int n) {
    if (ptr == n-1) return;
    else {
        for (int i=ptr;i<n-1;i++) {
            num[i]=1;
            check(num,n);
            dfs(num,i+1,n);
            num[i]=0;
            //cout<<"i:"<<i<<endl;
        }
    }
}

int main() {
    int t;
    cin>>t;
    
    cin>>n>>j;
    
    int num[16];
    
    for (int i=0;i<n;i++) {
        num[i]=0;
    }
    
    num[0]=1;
    num[n-1]=1;
    
    /*
    for (int i=2;i<=10;i++) {
        int num[6]={1,0,0,0,1,1};
        cout<<getNum(i,num)<<endl;
    }
    */
    
    cout << "Case #1:"<<endl;

    dfs(num,1,n);

    
    
    return 0;
}
