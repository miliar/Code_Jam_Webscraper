#include <stdio.h>
#include <iostream>

using namespace std;
int min(int &x, int &y){
    return x<y?x:y;
}
int main(){
    freopen("1a_a.large.in", "r", stdin);
    freopen("1a_a.large.out", "w", stdout);
    int T,N,m[1001];
    while(scanf("%d",&T)!=EOF){
        for(int k=1;k<=T;k++){
            scanf("%d",&N);
            for(int i=0;i<N;i++)scanf("%d",&m[i]);
            int y=0,z=0,max_span=0;
            for(int i=0;i<N-1;i++){
                if(m[i]>m[i+1])y+=m[i]-m[i+1];
            }
            for(int i=0;i<N-1;i++){
                max_span = max_span > (m[i]-m[i+1])?max_span:(m[i]-m[i+1]);
            }
            for(int i=0;i<N-1;i++){
                z+=min(max_span,m[i]);
            }
            printf("Case #%d: %d %d\n",k,y,z);
        }
    }
    return 0;
}
