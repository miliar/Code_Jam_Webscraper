#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
    int i,j,k,l;
    int t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int a,b;
        int n[4][4];
        int m[4][4];
        scanf("%d",&a);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&n[i][j]);
        }
        scanf("%d",&b);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&m[i][j]);
        }
        int co=0,ti=0;;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(n[a-1][i]==m[b-1][j])
                    {co++;ti=n[a-1][i];}
            }
        }
        if(co==0)
            {printf("Case #");printf("%d",k);printf(": Volunteer cheated!\n");}
        if(co==1)
            {printf("Case #");printf("%d",k);printf(": ");printf("%d\n",ti);}
        if(co>1)
            {printf("Case #");printf("%d",k);printf(": Bad magician!\n");}

    }
}
