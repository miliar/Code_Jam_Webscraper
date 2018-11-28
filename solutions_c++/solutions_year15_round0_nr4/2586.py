#include <cstdio>
#include <string>
using namespace std;
int T,i,X,R,C,winner;
int main()
{
    freopen("ProblemD.in","r",stdin);
    freopen("ProblemD.out","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d %d %d",&X,&R,&C);
        switch(X)
        {
            case 1:
                winner=1;
                break;
            case 2:
                winner=(R*C%2==0);
                break;
            case 3:
                winner=(R*C==6 || R*C==9 || R*C==12);
                break;
            case 4:
                winner=(R*C==12 || R*C==16);
                break;
        }
        printf("Case #%d: %s\n",i,winner?"GABRIEL":"RICHARD");
    }
    return 0;
}
