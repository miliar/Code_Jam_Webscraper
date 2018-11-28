#include<iostream>
#include<cstdio>
using namespace std;
int main() {
    freopen("SheepIn.txt","r",stdin);
    freopen("SheepOut.txt","w",stdout);
    int T,i,k,hash[10],flag;
    long long int N,ans,temp;
    scanf("%d",&T);
    for(k=1;k<=T;k++) {
        ans=-1;
        scanf("%lld",&N);
        if(N!=0) {
            for(i=0;i<10;i++) {
                hash[i]=0;
            }
            ans=N;
            flag=0;
            while(flag==0){
                temp=ans;
                flag=1;
                while(temp!=0) {
                    hash[temp%10]=1;
                    temp/=10;
                }
                for(i=0;i<10;i++) {
                    if(hash[i]==0) {
                        flag=0;
                        break;
                    }
                }
                ans+=N;
            }
        }
        if(ans==-1) {
            printf("Case #%d: INSOMNIA\n",k);
        } else {
            printf("Case #%d: %lld\n",k,ans-N);
        }
    }
    return 0;
}
