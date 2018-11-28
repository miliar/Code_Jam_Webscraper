#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T , A , B , K, Tn=0;
    long long ans=0;
    cin>>T;
    while(T--){
        ans=0; Tn++;

        cin>>A>>B>>K;
        for(int j=0;j<A;j++)
            for(int i=0;i<B;i++)
                if( (j&i) < K )
                    ans++;
        printf("Case #%d: %lld\n",Tn,ans);

    }
}
