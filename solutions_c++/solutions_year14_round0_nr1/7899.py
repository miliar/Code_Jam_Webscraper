#include<cstdio>
#include<cstring>

using namespace std;

int T,test,N,i,j;
int P[5][5],A[20],ok,last;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for(test=1; test<=T; test++)
    {
        ok=0;
        memset(A,0,sizeof(A));
        scanf("%d",&N);
        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
                scanf("%d",&P[i][j]);
        for(j=1; j<=4; j++)
            A[P[N][j]]++;
        scanf("%d",&N);
        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
                scanf("%d",&P[i][j]);
        for(j=1; j<=4; j++)
            A[P[N][j]]++;
        for(i=1; i<=16; i++)
            if(A[i]==2) ok++,last=i;
        printf("Case #%d: ",test);
        if(ok==0) printf("Volunteer cheated!\n");
        if(ok==1) printf("%d\n",last);
        if(ok>1) printf("Bad magician!\n");
    }

    return 0;
}
