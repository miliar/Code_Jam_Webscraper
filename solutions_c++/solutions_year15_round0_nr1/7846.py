//
//  main.cpp
//  opera
//
//  Created by Pongpanot Chuaysakun on 4/11/2558 BE.
//  Copyright (c) 2558 Pongpanot Chuaysakun. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int n=0;n<t;n++){
        int smax;
        cin>>smax;
        string s;
        cin>>s;
        int sum=0;
        int count=0;
        for(int i=0;i<=smax;i++)
        {
            if(sum>i){
                sum+=s[i]-48;
            } else {
                count += i-sum;
                sum += i-sum;
                sum+=(s[i]-48);
            }
        }
        cout<<"Case #"<<n+1<<": "<<count<<endl;
    }
}
