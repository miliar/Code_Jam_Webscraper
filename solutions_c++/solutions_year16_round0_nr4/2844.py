#include <stdio.h> 

using namespace std;

int main(){
    int T, K, C, S;    
    scanf("%d", &T);
    for(int t=1; t<=T; ++t) {
        printf("Case #%d: ",t);     
        scanf("%d%d%d", &K, &C, &S);
        for (int i=1; i<=K; ++i) printf("%d ",i);
        printf("\n");
    }
    return 0;
}
