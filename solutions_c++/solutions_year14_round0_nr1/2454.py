#include <iostream>
#include <fstream>

using namespace std;
int n;
int r1,r2;
int row1[5],row2[5];
int ok,p;
void citire()
{   int x;
    int k=1;
    scanf("%d ",&r1);
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {scanf("%d",&x);
         if(i==r1)
            row1[j]=x;
        }
    k=1;
    scanf("%d ",&r2);
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {scanf("%d",&x);
        if(i==r2)
            row2[j]=x;
        }
}
void rez()
{
    for(int j=1;j<=4;j++)
      for(int i=1;i<=4;i++)
        if(row1[j]==row2[i])
            ok++,p=row1[j];
    if(ok==1)
        printf("%d",p);
    else if(ok==0)
        printf("Volunteer cheated!");
    else printf("Bad magician!");
}

int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    scanf("%d ",&n);
    for(int run=1;run<=n;run++)
    {citire();
    printf("Case #%d: ",run);
    rez();
    printf("\n");
    ok=0;
    }
    return 0;
}
