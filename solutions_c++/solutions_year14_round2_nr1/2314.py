#include <cstdio>
#include <queue>
#include <stack>
#include <iostream>
#include <limits.h>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define MAXN 10000
#define INF INT_MAX //nao ha perigo de overflow

typedef struct char_n{
    char c;
    int count;
} Ch;

int main(){
    int t,n,k;
    char aux[110];
    Ch j[2][110];
    int max[10];
    int ans,q;

    scanf("%d", &t);
    for(int i = 0;i<t;i++){
        ans = 0;
        scanf("%d", &n);
        while(n--){
            scanf("%s", aux);
            k = 0;
            for(int m = 0;m<strlen(aux);m++){
                j[n][k].c = aux[m];
                j[n][k].count = 1;
                while(m+1<strlen(aux) && aux[m+1] == j[n][k].c){
                    j[n][k].count++;
                    m++;
                }
                //printf("%d\n",  j[n][k].count);
                k++;
            }
            max[n] = k;
        }
        printf("Case #%d:", i+1);
        if(max[0] != max[1])
            printf(" Fegla Won\n");
        else{
            for(int k = 0;k<max[0];k++){
                if(j[0][k].c != j[1][k].c){
                    printf(" Fegla Won\n");
                    ans = -1;
                    break;
                }else{
                    q = abs(j[0][k].count+j[1][k].count)/2;
                    ans+=abs(j[0][k].count-q)+abs(j[1][k].count-q);
                }
            }
            if(ans>=0){
                printf(" %d\n",ans);
            }

        }

    }

    return 0;
}