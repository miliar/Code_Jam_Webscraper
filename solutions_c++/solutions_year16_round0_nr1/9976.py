//
//  main.cpp
//  codejam
//
//  Created by Сыннер on 09.04.16.
//  Copyright (c) 2016 edu.self. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1e5;
const int M = 10;

bool f[N][M];


ull solve(int t){
    ull n;
    cin>>n;

    for(int i = 1;i<1e5;i++){
        ull a = n*i;
        while(a){
            int x = a%10;
            f[t][x] = true;
            a/=10;
        }
        bool flag = true;
        for(int j = 0;j<10;j++){
            if(!f[t][j]){
                flag = false; break;
            }
        }
        if(flag){
            return n*i;
        }
    }
    return 0;
}
int main(int argc, const char * argv[]) {
    //freopen("","r",stdin); freopen("","w",stdout);
    int t;
    cin>>t;
    int y = 0;
    while(t--){
        y++;
        ull ans = solve(t);
        cout<<"Case #"<<y<<": ";
        if(ans == 0) cout<<"INSOMNIA";
        else cout<<ans;
        cout<<'\n';
    }
    
    return 0;
}
