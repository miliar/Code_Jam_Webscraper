//
//  main.cpp
//  codejam_2016
//
//  Created by fchowdhu on 4/9/16.
//  Copyright © 2016 fchowdhu. All rights reserved.
//

#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<set>
#include<fstream>
#include<cfloat>
#include<cassert>
using namespace std;

typedef long long  LL;
typedef vector<int>   vi;
typedef pair<int,int>  pii;


long long f[200000];
long long s[200000];
long long arr[200000];
long long vis[200000];
#define MOD 1000000009
long long bm(long long a, long long p){
    if(p==0)return 1;
    else if(p%2==0){
        long long x = bm(a,p/2);
        x*=x;
        x%=MOD;
        return x;
    }else{
        long long x = bm(a,p-1);
        x*=a;
        x%=MOD;
        return x;
    }
}
long long ncr(long long n, long long r){
    
    long long ans = f[n];
    ans *= bm(f[n-r],MOD-2);
    ans%=MOD;
    ans *= bm(f[r],MOD-2);
    ans%=MOD;
   // cout<<n<<"--"<<r<<"--"<<ans<<endl;
    return ans;
}
int main() {
    int C=0;
    freopen("/Users/fchowdhu/Downloads/A-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/A-large.out", "w", stdout);
    int t, cn = 1;
    cin>>t;
    while(t--){
        int n;
        string str, str1;
        cin>>str>>n;
        str1 = str;
        int c = 0, c1 = 0;
        for (int i=0; i<=str.size()-n; i++) {
            if(str[i] == '-'){
                for (int j=0; j<n; j++) {
                    if(str[i+j] == '-')str[i+j] = '+';
                    else str[i+j] = '-';
                }
                c++;
            }
        }
        
        reverse(str1.begin(), str1.end());
        for (int i=0; i<=str1.size()-n; i++) {
            if(str1[i] == '-'){
                for (int j=0; j<n; j++) {
                    if(str1[i+j] == '-')str1[i+j] = '+';
                    else str1[i+j] = '-';
                }
                c1++;
            }
        }
        bool ans =true;
        for (int i=0; i<str.size(); i++){
            if(str[i] == '-')ans =false;
        }
        assert(!ans || c==c1);
        if (ans)cout<<"Case #"<<cn++<<": "<<max(c, c1)<<endl;
        else cout<<"Case #"<<cn++<<": IMPOSSIBLE"<<endl;
    }
    
    return 0;
}
