#include <bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
const int MX=1233;
void solve(int n , int cnt){
    n-=4;

    for(int mask=0;mask<cnt;mask++){
        cout<<"11";
        for(int j=0;j<n/2;j++){
            if(mask & (1<<j))
                cout<<"11";
            else cout<<"00";
        }
        cout<<"11 ";
        for(int j=2;j<=10;j++) cout<<j+1<<' ';
        puts("");
    }

}
int main(){
    /*#ifdef ONLINE_JUDGE
    freopen("high.in","r",stdin);
    freopen("high.out","w",stdout);
    #endif // ONLINE_JUDGE*/
    /*#ifndef ONLINE_JUDGE
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    #endif // ONLINE_JUDGE*/
    int T , Tn=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d:\n",++Tn);
        int n , k;
        cin>>n>>k;
        solve(n , k);
    }

}

