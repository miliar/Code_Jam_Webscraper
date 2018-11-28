#include <bits/stdc++.h>
using namespace std;
int bucket[11];
int T,N;
long long counter;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        for(int i=0;i<10;i++){
            bucket[i] = 0;
        }
        counter = 0;
        scanf("%d",&N);
        if(N==0){
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        long long mul = 1;
        long long temp;
        while(counter<10){
            temp = N*mul;
            long long hold = 1;
            while(hold<=temp){
                int x = (int)((temp/hold)%10);
                if(bucket[x]==0){
                    counter++;
                    bucket[x]=1;
                }
                hold *= 10;
            }
            mul++;
        }
        printf("Case #%d: %lld\n",t,temp);
    }
    return 0;
}
