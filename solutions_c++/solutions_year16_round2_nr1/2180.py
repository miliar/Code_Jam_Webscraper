#include<cstdio>
#include<cstring>
using namespace std;
int Q,test,n,p,cate,ras[15],v[50];
char s[2005];
const char  numar[][10]={"ZERO","ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d\n",&Q);
    for(test=1; test<=Q; test++)
    {
        printf("Case #%d: ",test);
        gets(s);
        n=strlen(s)-1;
        for(int i=0;i<=n;i++)
            v[s[i]-'A'+1]++;
        /// Zero 0
        p='Z'-'A'+1;
        cate=v[p];
        ras[0]=cate;
        for(int i=0;i<4;i++)
            v[numar[0][i]-'A'+1]-=cate;

        /// Two 2
        p='W'-'A'+1;
        cate=v[p];
        ras[2]=cate;
        for(int i=0;i<3;i++)
            v[numar[2][i]-'A'+1]-=cate;

        /// Six 6
        p='X'-'A'+1;
        cate=v[p];
        ras[6]=cate;
        for(int i=0;i<3;i++)
            v[numar[6][i]-'A'+1]-=cate;

        /// Eight 8
        p='G'-'A'+1;
        cate=v[p];
        ras[8]=cate;
        for(int i=0;i<5;i++)
            v[numar[8][i]-'A'+1]-=cate;

        /// Three 3
        p='T'-'A'+1;
        cate=v[p];
        ras[3]=cate;
        for(int i=0;i<5;i++)
            v[numar[3][i]-'A'+1]-=cate;

        /// Four 4
        p='R'-'A'+1;
        cate=v[p];
        ras[4]=cate;
        for(int i=0;i<4;i++)
            v[numar[4][i]-'A'+1]-=cate;

        /// Five 5
        p='F'-'A'+1;
        cate=v[p];
        ras[5]=cate;
        for(int i=0;i<4;i++)
            v[numar[5][i]-'A'+1]-=cate;

        /// Seven 7
        p='S'-'A'+1;
        cate=v[p];
        ras[7]=cate;
        for(int i=0;i<5;i++)
            v[numar[7][i]-'A'+1]-=cate;

        /// One 1
        p='O'-'A'+1;
        cate=v[p];
        ras[1]=cate;
        for(int i=0;i<3;i++)
            v[numar[1][i]-'A'+1]-=cate;

        /// Nine 9
        p='E'-'A'+1;
        cate=v[p];
        ras[9]=cate;
        for(int i=0;i<4;i++)
            v[numar[9][i]-'A'+1]-=cate;
        for(int i=0;i<=9;i++)
            for(int j=1;j<=ras[i];j++)
                printf("%d",i);
        printf("\n");
    }
    return 0;
}
