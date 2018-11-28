//
//  main.cpp
//  math
//
//  Created by Haoyang Gu on 2/2/16.
//  Copyright (c) 2016 Haoyang Gu. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>


using namespace std;

#define all(x) x.begin(),x.end()
 // sort(all(vec))
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define tr(container, it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
// tr(set,it)
    // total+=it->second;

set<int> se;

void cnt(long long y){
    while(y>0){
        se.insert(y%10);
        y/=10;
    }
    return ;
}

int main(){
    int t;
    cin >> t;
    int k=1;
    while(t--){
        se.clear();
        int n;
        cin >> n;
        cout << "Case #" << k++ << ": ";
        if(n==0){
            cout << "INSOMNIA\n";
            continue;
        }

        long long x=n;
        long long y=n;
        long long res;
        while(se.size()!=10){
            res=y;
            cnt(y);
            y=y+x;
        }
        cout << res << endl;
    }
}