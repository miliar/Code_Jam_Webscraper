#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int T,N;
string s;
int v[101010];

int calc(int x){
    int ret = 0;

    for(int i=1;i<=N;++i){
        if(v[i] > x) {
            ret += v[i] / x;
            if(v[i] % x == 0)
                --ret;
        }
    }
    return ret + x;
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> T;
    int tt = 0;
    while(T--){
        ++tt;

        cin>>N;
        int mmax = 0;
        long long sum = 0;
        for(int i=1;i<=N;++i){
            cin>>v[i];
            mmax = max(mmax,v[i]);
            sum += v[i];
        }

        int ret = mmax;
        for(int i=1;i<=mmax;++i){
            int cl = calc(i);
            if(cl >= 0){
                ret = min(ret, cl);
            }
        }
        if(sum == 0)
            ret = 0;
        printf("Case #%d: %d\n",tt, ret);
    }
    return 0;
}
