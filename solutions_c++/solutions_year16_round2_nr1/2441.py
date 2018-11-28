#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char str[2010];
int nub[30];

int ans[10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int te;
    scanf("%d",&te);
    for ( int T=1 ; T<=te ; T++ )
    {
        scanf("%s",str+1);
        int n = strlen(str+1);
        for ( int c=0 ; c<26 ; c++ )    nub[c] = 0;
        for ( int c=0 ; c<10 ; c++ )    ans[c] = 0;
        for ( int c=1 ; c<=n ; c++ )
        {
            nub[str[c]-'A']++;
        }
        ans[0] = nub[25];
        nub['O'-'A'] -= nub[25];
        ans[6] = nub['X'-'A'];
        nub['S'-'A'] -= nub['X'-'A'];
        ans[7] = nub['S'-'A'];
        nub['N'-'A'] -= nub['S'-'A'];
        ans[2] = nub['W'-'A'];
        nub['T'-'A'] -= nub['W'-'A'];
        nub['O'-'A'] -= nub['W'-'A'];
        ans[4] = nub['U'-'A'];
        nub['F'-'A'] -= nub['U'-'A'];
        nub['O'-'A'] -= nub['U'-'A'];
        ans[5] = nub['F'-'A'];
        ans[8] = nub['G'-'A'];
        nub['T'-'A'] -= nub['G'-'A'];
        ans[3] = nub['T'-'A'];
        ans[1] = nub['O'-'A'];
        nub['N'-'A'] -= nub['O'-'A'];
        ans[9] = nub['N'-'A']/2;
        printf("Case #%d: ",T);
        for ( int c=0 ; c<10 ; c++ )
        {
            for ( int d=1 ; d<=ans[c] ; d++ )   printf("%d",c);
        }
        printf("\n");
    }

}
