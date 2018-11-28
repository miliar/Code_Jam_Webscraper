#include <bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
const int MX=1233;
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
    long long n;
    while(T--){
        printf("Case #%d: ",++Tn);
        cin>>n;
        if(n==0){
            puts("INSOMNIA");
            continue;
        }
        int mask=0; long long cur=0;
        while(1){
            cur+=n;
            long long x = cur;
            while(x>0){
                long long mod = (x%10);
                mask|=(1<<mod);
                x/=10;
            }
            if(mask == 1023){
                cout<<cur<<endl;
                break;
            }
        }
    }

}
