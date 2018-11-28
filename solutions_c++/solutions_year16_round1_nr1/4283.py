#include <cstdio>
#include <cstring>
const int MN =2010;
int TestCase;
char s[MN],t[MN];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d", &TestCase);
    for(int O=1; O<=TestCase; O++){
        printf("Case #%d: ", O);
        scanf("%s", s);
        int N=(int)strlen(s);
        int L=N; int R=N;
        t[N]=s[0];
        for(int i=1; i<N; i++)
            if(s[i]>=t[L]) t[--L]=s[i];
                    else t[++R]=s[i];
        for(int i=L; i<=R; i++)
            printf("%c", t[i]);
        printf("\n");
    }
}
