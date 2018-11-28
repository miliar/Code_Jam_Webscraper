//
//  main.cpp
//  atcoder
//
//  Created by IshikawaTakumi on 2016/05/28.
//  Copyright © 2016年 IshikawaTakumi. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <set>
#include <functional>
#include <map>
#include <queue>
#include <cstring>
#include <stack>
#include <iomanip>
#include <climits>
#include <numeric>
using namespace std;
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define show(x) cout << #x << " = " << x << endl;
typedef long long ll;
typedef pair<int,int> P;
int n,m,q;
int main(){
    int t;
    cin >> t;
    for(int test = 1; test <= t; test ++){
        cout << "Case #" << test << ": ";
        string s;
        int k;
        cin >> s >> k;
        int n = (int)s.size();
        int ans = 0;
        for(int i = 0; i < n-k+1; i++){
            if(s[i]=='-'){
                ans++;
                for(int j = i;j <i+k; j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        bool flag = true;
        rep(i,n){
            if(s[i]=='-')flag = false;
        }
        if(flag){
            cout << ans << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
        
    }
}
