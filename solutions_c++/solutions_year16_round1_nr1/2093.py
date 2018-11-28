#include <cstdio>

using namespace std;

char s[20000];
char S[1000];

int main(void)
{
    int cases,cas;
    scanf("%d",&cases);
    int beg, end;

    for(cas=1;cas<=cases;cas++){
            beg = end = 10000;

            scanf("%s",S);
            s[beg] = S[0];
            for(int i=1;S[i];i++){
                if(S[i]>=s[beg]){
                    s[--beg] = S[i];
                }
                else{
                    s[++end] = S[i];
                }
            }

            printf("Case #%d: ",cas);

            for(int i=beg;i<=end;i++){
                printf("%c",s[i]);
            }
            printf("\n");

    }
    return 0;
}
