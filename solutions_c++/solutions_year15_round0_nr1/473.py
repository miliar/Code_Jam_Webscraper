#include<stdio.h>
#include<string.h>
#include<algorithm>
#define SIZ 1010
using namespace std;
char c[SIZ];
int cl, s;
int main(){
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int i, j=0, k=0;
        scanf("%d %s", &s, c);
        j=c[0]-'0';
        for(i=1; i<=s; i++){
            if(j<i){
                k+=i-j;
                j=i;
            }
            j+=c[i]-'0';
        }
        printf("Case #%d: %d\n", tt, k);
    }
    return 0;
}
