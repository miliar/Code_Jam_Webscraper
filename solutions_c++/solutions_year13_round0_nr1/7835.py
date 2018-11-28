#include<stdio.h>

int main()
{
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        char a[4][5],c;
        int i,j;
        int flag=1;
        for(i=0;i<4;i++)
        {
            scanf("%s",&a[i]);
        }
 /*       for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            printf("%c\n",a[i][j]);
        }
*/
        for(i=0;flag && i<4;i++)
        {
            j=1;
            if(a[i][0]=='.');
          //  printf("GGGGGGGGG");
            else
            {
            if(a[i][1]=='.');
            else if(a[i][0]=='T')
            {
                c=a[i][1];
                j++;
                flag=0;
            }
            else
            {c=a[i][0];
            flag=0;}
            for(;j<4;j++)
            {
                if(a[i][j]!=c && a[i][j]!='T')
                {
                    flag=1;
          //  printf("cc=%c a=%c",c,a[i][j]);
                    break;
                }
            }
            }
        }
        for(i=0;flag && i<4;i++)
        {
            j=1;
            if(a[0][i]=='.');
            else
            {
            if(a[1][i]=='.');
            else if(a[0][i]=='T')
            {
                c=a[1][i];
                j++;
                flag=0;
            }
            else
            {c=a[0][i];
            flag=0;}
            for(;j<4;j++)
            {
                if(a[j][i]!=c && a[j][i]!='T')
                {
                    flag=1;
                    break;
                }
            }
            }
        }
        if(flag)
        {
            i=1;
            j=1;
            if(a[0][0]=='.');
            else
            {
            if(a[1][1]=='.');
            else if(a[0][0]=='T')
            {
                c=a[1][1];
                i++;
                j++;
                flag=0;
            }
            else if(c!='.')
            {c=a[0][0];
            flag=0;}
            for(;j<4;j++)
            {
                if(a[i][j]!=c && a[i][j]!='T')
                {
                    flag=1;
                    break;
                }
                i++;
            }
            }
        }
  //      printf("flag=%d",flag);
        if(flag)
        {
            i=0;
            j=3;
            if(a[0][3]=='.');
            else
            {
            if(a[1][2]=='.');
            else if(a[0][3]=='T')
            {
                c=a[1][2];
                i++;
                j--;
                flag=0;
            }
            else
            {c=a[0][3];
            flag=0;}
            for(;i<4;i++)
            {
                if(a[i][j]!=c&&a[i][j]!='T')
                {
                    flag=1;
                    break;
                }
                j--;
            }
            }
        }
    //     printf("ffffffff=%d",flag);
        int flag1=0;
        for(i=0;!flag1 && i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='.')
                {
                    flag1=1;
                    break;
                }
            }
        }
        if(!flag)
        {
            if(c=='O')
            printf("Case #%d: O won\n",k);
            else
            printf("Case #%d: X won\n",k);
        }
        else
        {
            if(flag1)
            printf("Case #%d: Game has not completed\n",k);
            else
            printf("Case #%d: Draw\n",k);
        }
    }
}
