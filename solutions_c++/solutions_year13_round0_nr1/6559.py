#include<iostream>
#include<stdio.h>
using namespace std;

int findT(char a[][4],int*,int*);
int matched(char a[][4], char, int ,int,int);
int isempty(char a[][4]);
int main()
{
	freopen("Al.in","rt",stdin);
	freopen("Al.out","wt",stdout);
    int no_of_cases,T_row=0,T_col=0,i,j,k,found=0;
    char garb;
    char a[4][4];
	scanf("%d",&no_of_cases);
	scanf("%c",&garb);
	for(i=1;i<=no_of_cases;i++)
	{
        for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {
                    scanf("%c", &a[j][k]);
                }
                scanf("%c",&garb);
            }
        scanf("%c",&garb);
       // scanf("%c",&garb);
      //  for(int g=0;g<4;g++)
        //  {for(int h=0;h<4;h++){
          //    printf(" %c",a[g][h]);
          //}
          //printf("\n");
          //}
          //printf("\n");
        found = findT(a,&T_row,&T_col);
        if(matched(a,'X',T_row,T_col,found))
            printf("Case #%d: X won\n",i);
        else if(matched(a,'O',T_row,T_col,found))
            printf("Case #%d: O won\n",i);
        else if(isempty(a))
            printf("Case #%d: Game has not completed\n",i);
        else
            printf("Case #%d: Draw\n",i);

	}
return 0;
}

int findT(char a[][4],int *p,int *q)
{
    int j,k;
     for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {
                   if(a[j][k]=='T')
                   {
                    *p=j;
                    *q=k;
                    return 1;
                   }
                }
            }
    return 0;
}

int matched(char a[][4], char ch, int p_row,int p_col,int found)
{
    int i;
    if(found==1)
    a[p_row][p_col]=ch;

    int flag = 0;
    for(i=0;i<4;i++)
    {
        if(((a[i][0]==ch)&&(a[i][1]==ch)&&(a[i][2]==ch)&&(a[i][3]==ch))||((a[0][i]==ch)&&(a[1][i]==ch)&&(a[2][i]==ch)&&(a[3][i]==ch)))
        {
            flag=1;
            return flag;
        }
    }
    if(((a[0][0]==ch)&&(a[1][1]==ch)&&(a[2][2]==ch)&&(a[3][3]==ch))||((a[0][3]==ch)&&(a[1][2]==ch)&&(a[2][1]==ch)&&(a[3][0]==ch)))
        flag =1;
    if(found==1)
    a[p_row][p_col]='T';
    return flag;
}



int isempty(char a[][4])
{
    int j,k;
     for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {
                   if(a[j][k]=='.')
                   {
                    return 1;
                   }
                }
            }
        return 0;
}

