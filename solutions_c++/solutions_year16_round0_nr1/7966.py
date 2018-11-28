//
//  0.cpp
//  0
//
//  Created by Apple on 3/12/16.
//  Copyright © 2016 ;. All rights reserved.
//

#include <algorithm>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <deque>
#include <queue>

using namespace std;

#define ll long long
#define maxn 100111
#define maxx 1000000000

bool is[10];
ll nis = 0;

void up(ll x){
    while(x>0){
        ll tmp = x%10;
        if(!is[tmp]){
            is[tmp] = 1;
            nis++;
        }
        x /= 10;
    }
}

int main(){
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt","w",stdout);
    
    int ntest;
    cin >> ntest;
    for(int test=1;test<=ntest;test++){
        ll n;
        cin >> n;
        if(n==0){
            printf("Case #%d: INSOMNIA\n",test);
            continue;
        }
        memset(is,0,sizeof(is));
        nis = 0;
        ll res=0;
        while(true){
            res++;
            up(res*n);
            if(nis == 10) break;
        }
        cout << "Case #" << test << ": "<< res*n << endl;
    }
}