//
// Created by 王若璇 on 16/4/9.
//
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
const int max_n = 1100000;
typedef long long ll;
bool visit[11];
ll ten[10] = {1,10,100,1000,10000,100000,1000000,10000000};
ll num[max_n];
int cnt = 0;
int getNum(ll n){
    int num = 0;
    while (n>0){
        n/=10;
        num++;
    }
    return num;
}
void solveNum(ll n){
    while (n>0){
        ll tmp = n%10;
        if(!visit[tmp]){
            visit[tmp] = true;
            //cout<<"tmp "<<tmp<<" cnt "<<cnt<<endl;
            cnt++;
        }
        n/=10;
    }
}
int solve(ll n){
    int num = getNum(n);
    ll tmpn = n;
    ll up = tmpn*ten[num+1];
    int step = 0;
    if(n==0){
        return 0;
    }
    while (tmpn<=up){
        solveNum(tmpn);
        //cout<<"tmpn "<<tmpn<<endl;
        step++;
        if(cnt==10){
            return step;
        }
        tmpn+=n;
    }
    return 0;


}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tCase;
    cin>>tCase;
    int tID = 0;
    while (tCase--){
        cout<<"Case #"<<++tID<<": ";
        ll n;
        memset(visit,0, sizeof(visit));
        cin>>n;
        cnt = 0;
        int res = solve(n);
        if(res==0){
            cout<<"INSOMNIA"<<endl;
        } else{
            cout<<res*n<<endl;
        }

    }
    return 0;
}
