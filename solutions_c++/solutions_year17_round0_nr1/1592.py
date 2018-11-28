#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-debug.out","wt",stdout);
    int T, N, K;
    char S[1111], P[1111];
    scanf("%d",&T);
    for(int f=1;f<=T;f++){
        memset(S,0,sizeof(S));
        memset(P,0,sizeof(P));
        getchar();
        scanf("%s %d",S,&K);
        N=strlen(S);
        strcpy(P,S);
        int ans=0, flag=1;
        for(int i=0;i<=N-K;i++){
            if(P[i]=='-'){
                for(int j=i;j<i+K;j++){
                    P[j]='+'+'-'-P[j];
                }
                ++ans;
            }
        }
        for(int i=N-K+1;i<N;i++) flag&=(P[i]=='+');
        printf("Case #%d: ",f);
        flag?printf("%d\n",ans):puts("IMPOSSIBLE");
    }
}
