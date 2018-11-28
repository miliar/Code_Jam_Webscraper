#include<stdio.h>
int main()
{
    int T,i,j,countt,countx,counto,p,q,b=0;
    char a[4][4];
    char f;
   // freopen("input.txt",stdin);
  //  freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
       for(i=0;i<4;i++)
       {
        getchar();
         for(j=0;j<4;j++)
          scanf("%c",&a[i][j]);
       }
       scanf("%c",&f);
        p=0; //标记是否分出胜负
        q=0;//记录有多少个字母
        for(i=0;i<4;i++)//判断行
        {
            countt=counto=countx=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='X')
                 {countx++;q++;}
                else if(a[i][j]=='O')
                 {counto++;q++;}
                else if(a[i][j]=='T')
                 {countt++;q++;}
            }
            if(countt+counto==4||counto==4)
            {
                p=1;
                printf("Case #%d: O won\n",++b);
                break;
            }
            else if(countt+countx==4||countx==4)
            {
                p=1;
                printf("Case #%d: X won\n",++b);
                break;
            }
        }
        if(p==0)
        {
            for(i=0;i<4;i++)//判断列
            {
                countt=countx=counto=0;
                for(j=0;j<4;j++)
                {
                    if(a[j][i]=='X')
                     countx++;
                    else if(a[j][i]=='O')
                     counto++;
                    else if(a[j][i]=='T')
                     countt++;
                }
                if(countt+countx==4||countx==4)
                {
                    p=1;
                    printf("Case #%d: X won\n",++b);
                    break;
                }
                else if(countt+counto==4||counto==4)
                {
                    p=1;
                    printf("Case #%d: O won\n",++b);
                    break;
                }
            }
        }
        if(p==0)
        {
            countt=counto=countx=0;
            for(i=0;i<4;i++) //判断主对角线
            {
                if(a[i][i]=='X')
                countx++;
                else if(a[i][i]=='O')
                counto++;
                else if(a[i][i]=='T')
                countt++;
            }
            if(countt+countx==4||countx==4)
            {
                p=1;
                printf("Case #%d: X won\n",++b);
            }
            else if(countt+counto==4||counto==4)
            {
                p=1;
                printf("Case #%d: O won\n",++b);
            }
        }
        if(p==0)
        {
            countt=counto=countx=0;
            for(i=0;i<4;i++) //判断次对角线
            {
                if(a[i][3-i]=='X')
                countx++;
                else if(a[i][3-i]=='O')
                counto++;
                else if(a[i][3-i]=='T')
                countt++;
            }
            if(countt+countx==4||countx==4)
            {
                p=1;
                printf("Case #%d: X won\n",++b);
            }
            else if(countt+counto==4||counto==4)
            {
                p=1;
                printf("Case #%d: O won\n",++b);
            }
        }
        if(p==0&&q==16)
         printf("Case #%d: Draw\n",++b);
        else if(p==0&&q!=16)
         printf("Case #%d: Game has not completed\n",++b);
    }
    return 0;
}
