#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("Bsmall.txt","w",stdout);
    int T,n,i,j,ncase;
    ncase = 0;
    cin>>T;
    int A,B,K;
    while(T--){
        ncase++;
        scanf("%d%d%d",&A,&B,&K);
        int ans = 0;
        for(i=0;i<A;i++){
            for(j=0;j<B;j++){
                int temp = i&j;
                if(temp<K) ans++;
            }
        }
        printf("Case #%d: %d\n",ncase,ans);
    }
    return 0;
}
