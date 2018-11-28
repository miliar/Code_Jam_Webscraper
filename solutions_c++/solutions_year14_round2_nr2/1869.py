//
//  main.cpp
//  lotterySmall
//
//  Created by Minghui Liu on 5/3/14.
//  Copyright (c) 2014 Minghui Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

void solve(int i, int a, int b, int k){
    int j, t;
    int count = 0;
    for(j=0;j<a;j++){
        for(t=0;t<b;t++){
            if((j&t)<k){
                count++;
            }
        }
    }
    cout << "Case #"<<i+1<<": "<<count<<endl;
}



int main(int argc, const char * argv[])
{
    freopen("/Users/minghui/Documents/C++/lotterySmall/lotterySmall/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/minghui/Documents/C++/lotterySmall/lotterySmall/B-small-attempt0.out.txt", "w", stdout);
    int T;
    cin >> T;
    int i;
    for(i=0;i<T;i++){
        int a, b, k;
        cin >> a>> b>> k;
        solve(i,a,b,k);
    }
    return 0;
}

