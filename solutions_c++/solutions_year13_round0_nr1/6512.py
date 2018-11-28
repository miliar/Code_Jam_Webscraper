#include<stdio.h>

int arr[4][4];
int rowX[4];
int colX[4];
int rowO[4];
int colO[4];
int flag;
int dialX;
int diarX;
int dialO;
int diarO;
int ans;

int main()
{
    int t;
    int i,j,k,l;
    char garbage;
    
    scanf("%d",&t);
    
    for(k=1;k<=t;k++)
    {
        for(i=0;i<=3;i++)
        {
            rowX[i]=0;
            rowO[i]=0;
            colX[i]=0;
            colO[i]=0;
        }
        ans=0;
        flag=0;
        dialX=0;
        dialO=0;
        diarO=0;
        diarX=0;
        
        for(i=0;i<=3;i++)
        {
            scanf("%c",&garbage);
            for(j=0;j<=3;j++)
            {
                l=i+j;
                scanf("%c",&arr[i][j]);
                if(arr[i][j]=='X')
                {
                    if(i==j)dialX++;
                    if(l==3)diarX++;
                    rowX[i]++;
                    colX[j]++;
                }
                else
                {
                    if(arr[i][j]=='O')
                    {
                        if(i==j)dialO++;
                        if(l==3)diarO++;
                        rowO[i]++;
                        colO[j]++;
                    }
                    else
                    {
                        if(arr[i][j]=='T')
                        {
                            if(i==j)dialX++;
                            if(l==3)diarX++;
                            if(i==j)dialO++;
                            if(l==3)diarO++;
                            rowO[i]++;
                            rowX[i]++;
                            colO[j]++;
                            colX[j]++;
                        }
                        else
                        {
                            if(arr[i][j]=='.')
                            {
                                flag=1;
                            }
                        }
                    }
                }
            }
        }
        
        for(i=0;i<=3;i++)
        {
            //printf("%d %d %d %d\n",rowX[i],colX[i],rowO[i],colO[i]);
            if(rowX[i]==4||colX[i]==4)ans=1;
            else
            {
                if(rowO[i]==4||colO[i]==4)ans=2;
            }
        }
        //printf("%d %d %d %d\n",dialX,dialO,diarX,diarO);
        if(ans==0)
        {
            if(dialX==4||diarX==4)ans=1;
            else
            {
                if(dialO==4||diarO==4)ans=2;
            }
        }
        if(ans==0)
        {
            if(flag==1)ans=4;
            else ans=3;
        }
        
        if(ans==1)printf("Case #%d: X won\n",k);
        if(ans==2)printf("Case #%d: O won\n",k);
        if(ans==3)printf("Case #%d: Draw\n",k);
        if(ans==4)printf("Case #%d: Game has not completed\n",k);
        scanf("%c",&garbage);
    }
    
    return 0;
}
