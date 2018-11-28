#include<bits/stdc++.h>
using namespace std;
#define read freopen("A-large.in","r",stdin)
#define write freopen("output2.txt","w",stdout)

bool digit[10];
unsigned long long N, M, i, cnt;

unsigned long long solve(){
    cnt=0, i=1;
    memset(digit,0,sizeof(digit));
    while(cnt<=10){
        M=i*N;
        while(M){
            int k=M%10;
            if(!digit[k]){
                digit[k]=1;
                cnt++;
            }
            M=M/10;
        }
        if(cnt==10) return i*N;
        i++;
    }
}

int main(){
    read;
    write;
    int T, t=1;
    scanf("%d", &T);
    while(T--){
        scanf("%llu", &N);
        if(N==0) printf("Case #%d: INSOMNIA\n", t++);
        else printf("Case #%d: %llu\n", t++, solve());
    }
    return 0;
}
