#include<cstdio>
#include<algorithm>
#define LL long long
using namespace std;

int T,X,N,A[10010],i,SOL,st,dr;

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        scanf("%d%d",&N,&X);
        SOL = 0;
        for(i=1;i<=N;i++)scanf("%d",&A[i]);
        sort(A+1,A+N+1);
        st=1;dr = N;
        while(st<=dr)
        {
            if(A[st]+A[dr] <= X)
            {
                SOL++;
                st++;
                dr--;
                continue;
            }
            dr--;
            SOL++;
        }
        printf("%d\n",SOL);
    }
    return 0;
}
