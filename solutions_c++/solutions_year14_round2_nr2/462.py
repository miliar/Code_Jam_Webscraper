#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
LL A, B, C;
LL memo[33][2][2][2][2][2][2];
LL cnt(int idx, int bA, int bB, int bR, int  lA, int lB, int  lC){
    if(idx < 0){
        if(lA && lB && lC)return 1;
        return 0;
    }
    LL &ans = memo[idx][bA][bB][bR][lA][lB][lC];
    if(ans != -1)return ans;

    ans = 0ll;

    int xA = (A>>idx)&1ll;
    int xB = (B>>idx)&1ll;
    int xC = (C>>idx)&1ll;

    //cout<<idx<<" "<<xA<<" "<<xB<<" "<<xC<<endl;

    for(int i = 0; i < 2; i++){
        for(int j = 0; j< 2; j++){
            int nlA = lA, nlB = lB, nlC = lC;
            int bit = i&j;
            if(!lA && i < xA)nlA = 1;
            if(!lB && j < xB)nlB = 1;
            if(!lC && bit < xC)nlC = 1;

            //if(nlA && nlB && nlC)cout<<idx<<" "<<i<<" "<<j<<endl;

            if((!lA && i > xA) || (!lB && j>xB))continue;
            if(!lC && bit > xC)continue;
            ans += 1ll*cnt(idx-1, i, j, bit, nlA, nlB, nlC);
        }
    }
    return ans;
}
int main(){
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++){
        cin>>A>>B>>C;
        int x = 0;
        for(int i=0;i<40;i++){
            if((A>>i)&1)x=i;
            if((B>>i)&1)x=i;
            if((C>>i)&1)x=i;
        }
        memset(memo, -1, sizeof(memo));
        printf("Case #%d: ", t);
        cout<<cnt(x,0,0,0,0,0,0)<<endl;
    }
    return 0;
}
