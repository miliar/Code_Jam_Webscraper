#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#define mem(a) memset( a, 0, sizeof(a) )
using namespace std;

char a[10005];
char ch[10050];

int main()
{
    int st, ed, i, j, n;
    int T, cas = 1;
    freopen("A-large(1).in", "r", stdin);
    freopen("out.txt", "w", stdout );
    scanf("%d", &T);
    while( T -- ){
        scanf("%s", ch);
        st = ed = 2000;
        a[st] = ch[0];
        for( i = 1; i < strlen(ch); i ++ ){
            if( ch[i] >= a[st] ){
                a[--st] = ch[i];
            }
            else a[++ed] = ch[i];
        }
        printf("Case #%d: ", cas++);
        for( i = st; i <= ed; i ++ )printf("%c", a[i]);
        puts("");
    }
}

