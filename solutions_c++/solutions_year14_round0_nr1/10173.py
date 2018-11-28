#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
   // freopen("A-small-attempt1 (1).in","r",stdin);
    //freopen("aaa.txt","W",stdout);

    int n,counter,f_r,i,j,s_r,a[5][5],b[5][5],temp[5],chk,x,value;
    scanf("%d",&n);
    for(counter=1;counter<=n;counter++)
    {
        scanf("%d",&f_r);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&s_r);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        for(i=1;i<=4;i++)
        {
            x=0;
            for(j=1;j<=4;j++)
            {
                if(a[f_r][i]==b[s_r][j])
                    x=a[f_r][i];
            }
        if(x==0)
            temp[i]=0;
        else
            temp[i]=x;
        }
    chk=0;
    for(i=1;i<=4;i++)
        if(temp[i]!=0)
            {
                chk++;
                value=temp[i];
            }
    if(chk==0)
        printf("Case #%d: Volunteer cheated!\n",counter);
    else if(chk==1)
        printf("Case #%d: %d\n",counter,value);
    else
        printf("Case #%d: Bad magician!\n",counter);
    }
return 0;
}
