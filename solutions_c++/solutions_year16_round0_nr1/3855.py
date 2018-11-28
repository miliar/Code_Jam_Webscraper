#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>
#include<queue>
#include<iostream>
typedef long long ll;
using namespace std;

int main(){
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int t, ca = 1, n;scanf("%d", &t);
    while(t--){
        int now = 0;
        scanf("%d", &n);
//        n = ca;
        printf("Case #%d: ", ca++);
        if(n == 0){
            puts("INSOMNIA");
            continue ;
        }
        ll sum = 0, ret;
        int vis = 0;
        for(int i = 1; ; i++){
            sum += n;
            ret = sum;
            while(ret){
                vis |= 1<<(ret%10);
                ret /= 10;
            }
            if( vis == (1<<10)-1 ){
                cout<<sum<<endl;
                break;
            }
        }
    }
    return 0;
}
