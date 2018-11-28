#include<stdio.h>

int main()
{
int t,j,x1,y,z;
freopen("output.txt", "w",stdout);
freopen("input.txt", "r",stdin);
scanf("%d",&t);
for (j=1;j<=t;j++)
{
    scanf("%d %d %d",&x1,&y,&z);
    if (x1==1)
    printf("Case #%d: GABRIEL\n",j);
    else if (x1==2 &&y*z%x1==0)
    printf("Case #%d: GABRIEL\n",j);
    else if (x1==2 &&y*z%x1!=0)
    printf("Case #%d: RICHARD\n",j);
    else if (x1==3 &&((y==2 && z==3)||(y==3 && z==2)||(y==4 && z==3)||(y==3 && z==4)||(y==3 && z==3)))
    printf("Case #%d: GABRIEL\n",j);
    else if (x1==3)
    printf("Case #%d: RICHARD\n",j);
    else if (x1==4 &&((y==4 && z==3)||(y==3 && z==4)||(y==4 && z==4)))
    printf("Case #%d: GABRIEL\n",j);
    else if (x1==4)
    printf("Case #%d: RICHARD\n",j);
}
    return 0;
}
