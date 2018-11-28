//
//  main.cpp
//  revengeofpancake
//
//  Created by HuMing on 4/9/16.
//  Copyright © 2016 HuMing. All rights reserved.
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<iostream>
using namespace std;
typedef long long ll;

int main(){
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-large.out", "w", stdout);
    ll T;
    cin >> T;
    for(ll t = 1; t <= T; t++){
        string str;
        cin>>str;
        ll sum=0;
        unsigned long a;
        a=str.length();
        for (ll i=0;i<a-1;i++){
            if(str[i]!=str[i+1]){
//                cout<<"string before: "<<str<<endl;
                for (ll j=0;j<i+1;j++){
                    str[j]=str[i+1];
                }
                sum+=1;
//                cout<<"here is string: "<<str<<endl;
                continue;
            }
        }

        if (str[a-1]=='-'){
            sum+=1;
        }
        cout << "Case #" << t << ": ";
        cout<<sum<<endl;
    }
}
