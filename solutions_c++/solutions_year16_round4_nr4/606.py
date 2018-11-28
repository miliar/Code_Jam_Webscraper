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
using namespace std;

typedef long long  LL;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
map<long long, int > vis;
double mem[202][102][102];
int tc[202][102][102], TC, n;
double P[222];
double solve(int ind, int k1, int k2){
    if(k1==0 && k2==0){
        return 1;
    }else if(ind == n || k1<0 ||k2<0) return 0;
    
    if(tc[ind][k1][k2] == TC) {
        
        return mem[ind][k1][k2];
    }
    tc[ind][k1][k2] = TC;
    double &ret  = mem[ind][k1][k2];
    ret = 0;
    for(int i=ind+1;i<n;i++)
    double ret1 = P[ind] * solve(ind+1, k1-1, k2);
    //ret1+= (1.-P[ind]) * solve(ind+1, k1, k2-1);
    //ret = max(ret, ret1);
    return ret;
}
int arr[10][10],ord[11],mac[11];
bool dfs(int N, int d=0){
    int bb =false;
    if(d== N) return true;
    for(int i=0;i<N;i++){
        if(ord[i]==0){
            ord[i]=1;
            for(int j=0;j<N;j++){
                if(mac[j] ==0 &&arr[i][j]){
                    mac[j] =1;
                    bool b = dfs(N,d+1);
                    if(b == false) return false;
                    else bb = true;
                    mac[j] =0;
                }
            }
            
            
            ord[i] = 0;
        }
    }
    return bb;
}
int check(int N, int msk){
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(msk&(1<<(i*(N)+ j))){
                arr[i][j] = 1;
            }else arr[i][j] = 0;
        }
        ord[i] =0;
        mac[i] = 0;
    }
    return dfs(N);
}
double BruteB(int k){
    double ret = 0;
    for(int i=0;i<(1<<n);i++){
        int c=0;
        for(int j=0;j<n;j++){
            if(i&(1<<j))c++;
        }
        if(c == k){
            TC++;
            //ret = max(solve(0, k/2, k/2, i), ret);
        }
    }
    return ret;
}
int get_input(){
    int N;
    cin>>N;
    string str[11];
    for(int i=0;i<N;i++){
        cin>>str[i];
    }
    int ans = 1e9;
    for(int i=0;i<(1<<(N*N));i++){
        int c=0;
        bool ok = true;
        for(int j=0;j<N;j++)
            for(int k=0;k<N;k++){
                if(i&(1<<(j*(N)+ k))){
                    arr[j][k] = 1;
                    
                }else arr[j][k] = 0;
                if(arr[j][k]==0 && str[j][k] =='1') ok = false;
                if(arr[j][k]==1 && str[j][k] =='0')c++;
            }
            if(ok){
                if(check(N, i)){
                    
                    ans = min(ans, c);
                }
            }
    }
        return ans;
    
}
int main() {
    freopen("/Users/fchowdhu/Downloads/D-small-attempt0.in", "r", stdin);
    //freopen("/Users/fchowdhu/Downloads/A-large.in", "r", stdin);
    freopen("/Users/fchowdhu/Downloads/D0.out", "w", stdout);
    int t,cn=1;
   // srand (time(NULL));

    cin>>t;
    

    while (t--) {
        TC++;
        int k;
        //cin>>n>>k;
        
        /*for (int i=0; i<n; i++) {
            cin>>P[i];
        }*/
        
        cout<<"Case #"<<cn++<<": ";
        
       // printf(" %.15lf", BruteB(k));
        cout<<get_input();
        
        cout<<endl;
    }
    
    return 0;
}
