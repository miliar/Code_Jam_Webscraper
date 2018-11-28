#include <stdio.h>

// 1=h -1=l -i=m -j=n -k=o
const char mul[8][8] = {
      //   h   i   j   k   l   m   n   o
/* h */ { 'h','i','j','k','l','m','n','o' },
/* i */ { 'i','l','k','n','m','h','o','j' },
/* j */ { 'j','o','l','i','n','k','h','m' },
/* k */ { 'k','j','m','l','o','n','i','h' },
/* l */ { 'l','m','n','o','h','i','j','k' },
/* m */ { 'm','h','o','j','i','l','k','n' },
/* n */ { 'n','k','h','m','j','o','l','i' },
/* o */ { 'o','n','i','h','k','j','m','l' },
    };

#define MUL(A,B) ( mul[(A) - 'h'][(B) - 'h'] )

int L;
long long X;
char s[10010];
char first[10010];
char last[10010];
char middle[10010][10010];
char all[20];

int solve()
{
    scanf("%d%I64d%s", &L, &X, s);
    //printf("%I64d", X);

    first[0] = last[0] = 'h';
    for(int i = 1; i <= L; i++){
        first[i] = MUL(first[i-1], s[i-1]);
        last[i] = MUL(s[L-i], last[i-1]);
        }

    all[0] = 'h';
    for(int i = 1; i <= 16; i++)
        all[i] = MUL(all[i-1], first[L]);

    for(int i = 0; i <= L; i++){
        middle[i][i] = 'h';
        for(int j = i+1; j <= L; j++)
            middle[i][j] = MUL(middle[i][j - 1], s[j - 1]);
        }

    if(X > 16)
        X = (X - 16) % 4 + 16;

    for(int m = 0; m < X; m++)
        for(int i = 0; i < L; i++)
            if (MUL(all[m], first[i]) == 'i')
                for(int j = i+1; j <= L; j++)
                    if ( middle[i][j] == 'j'
                        && MUL(last[L-j], all[X-m-1]) == 'k'
                        )
                        return 1;

    for(int m = 0; m < X - 1; m++)
        for(int i = 0; i <= L; i++)
            if (MUL(all[m], first[i]) == 'i')
                for(int n = m+1; n < X; n++)
                    for(int j = 0; j <= L; j++)
                        if ( MUL( MUL(last[L - i], all[n-m-1]) , first[j] ) == 'j'
                            && MUL(last[L - j], all[X-n-1]) == 'k'
                            )
                            return 1;

    return 0;
}


int main()
{
    int t, t0;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        printf("Case #%d: %s\n", t0 + 1, solve() ? "YES" : "NO");
        }
    return 0;
}
