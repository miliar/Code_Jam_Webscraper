#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<unordered_map>
using namespace std;
int main(void){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int l; int T;
    scanf("%i",&T);
    char c;
    scanf("%c", &c);
    for(l=0;l<T;l++){
        printf("Case #%i: ", l+1);
        char S[2000];
        int i;
        int N;
        for(i=0;;i++){
            scanf("%c", &S[i]);
            if(S[i]=='\n'){N=i; break;}
        }
        char za[2000];
        int z=0;
        za[0]=S[0];
        char pred[2000];
        int p=0;
        pred[0]=S[0];
        for(i=1;i<N;i++){
            if(S[i]>=pred[p]){
                pred[p+1]=S[i];
                p++;
            }
            else{
                za[z+1]=S[i];
                z++;
            }
        }
        for(i=p;i>0;i--){
            printf("%c", pred[i]);
        }
        for(i=0;i<=z;i++){
            printf("%c", za[i]);
        }
        printf("\n");
    }
    return 0;
}
