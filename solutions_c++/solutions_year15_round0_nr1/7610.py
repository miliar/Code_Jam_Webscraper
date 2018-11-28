#include<cstdio>
using namespace std;

char shy[1005];

int main(){

    int t, ca = 1, s, p, need;
    scanf("%d", &t);

    while(ca<=t){
        scanf("%d%*c", &s);
        gets(shy);
        need = 0;
        p = shy[0]-'0';
        for(int i=1; i<=s; i++){
            if(p<i){
                p++;
                need++;
            }p += shy[i]-'0';
        }
        printf("Case #%d: %d\n", ca++, need);
    }

    return 0;
}
