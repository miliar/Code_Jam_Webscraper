#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
   char a[4][5];
   int t,i,j,k,f=0,s;
   //scanf("%d",&t);
   cin>>t;
   for(i=1;i<=t;i++)
   {
	f=0;
    for(j=0;j<4;j++)
    {
	//scanf("%c%c%c%c",&a[j][0],&a[j][1],&a[j][2],&a[j][3]);
	//printf("input loop");
	cin>>a[j];
        a[j][4]='\0';
        
    }
    // for rows
    for(j=0;j<4;j++)
    {


        for(k=0;k<4;k++)
        {if(f!=1)
         if(a[j][k]=='X'||a[j][k]=='T')
         {
             if((a[j][k+1]=='X'||a[j][k+1]=='T')&&(a[j][k+2]=='X'||a[j][k+2]=='T')&&(a[j][k+3]=='X'||a[j][k+3]=='T'))
             {
                 printf("Case #%d: X won\n",i);
                 f=1;
             }
         }
	if(f!=1)
        if(a[j][k]=='O'||a[j][k]=='T')
         {
             if((a[j][k+1]=='O'||a[j][k+1]=='T')&&(a[j][k+2]=='O'||a[j][k+2]=='T')&&(a[j][k+3]=='O'||a[j][k+3]=='T'))
             {
                 printf("Case #%d: O won\n",i);
                 f=1;
             }
         }
        }
    }
    // for columns
        for(j=0;j<4;j++)
    {


        for(k=0;k<4;k++)
        {if(f!=1)
         if(a[k][j]=='X'||a[k][j]=='T')
         {
             if((a[k+1][j]=='X'||a[k+1][j]=='T')&&(a[k+2][j]=='X'||a[k+2][j]=='T')&&(a[k+3][j]=='X'||a[k+3][j]=='T'))
             {
                 printf("Case #%d: X won\n",i);
                 f=1;
             }
         }
	if(f!=1)
        if(a[k][j]=='O'||a[k][j]=='T')
         {
             if((a[k+1][j]=='O'||a[k+1][j]=='T')&&(a[k+2][j]=='O'||a[k+2][j]=='T')&&(a[k+3][j]=='O'||a[k+3][j]=='T'))
             {
                 printf("Case #%d: O won\n",i);
                 f=1;
             }
         }
        }
    }

// for diagonal
    j=0;
if(f!=1)
    if((a[j][j]=='X'||a[j][j]=='T')&&(a[j+1][j+1]=='X'||a[j+1][j+1]=='T')&&(a[j+2][j+2]=='X'||a[j+2][j+2]=='T')&&(a[j+3][j+3]=='X'||a[j+3][j+3]=='T'))
        {printf("Case #%d: X won\n",i);
        f=1;
        }
if(f!=1)
    if((a[j][j]=='O'||a[j][j]=='T')&&(a[j+1][j+1]=='O'||a[j+1][j+1]=='T')&&(a[j+2][j+2]=='O'||a[j+2][j+2]=='T')&&(a[j+3][j+3]=='O'||a[j+3][j+3]=='T'))
        {printf("Case #%d: O won\n",i);
        f=1;
        }
    j=0;
if(f!=1)
    if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
        {printf("Case #%d: X won\n",i);
        f=1;
        }
if(f!=1)
    if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
        {printf("Case #%d: O won\n",i);
        f=1;
        }
// for draw
    if(f!=1)
    {
        //s=f;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(a[j][k]=='.')
                {
                    f=2;
//printf("Case #%d: Game has not completed\n",i);
                    break;
                }
            }
        }
        if(f!=2)
        {
            printf("Case #%d: Draw\n",i);
            //f=s;
        }
    }
    if(f==2)
  printf("Case #%d: Game has not completed\n",i);
//printf("\n f=%d \n",f);
   }

   return 0;
}
