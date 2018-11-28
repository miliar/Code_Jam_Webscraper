#include<stdio.h>
#include<conio.h>
int main()
{
    int t;
    int save1[5],save2[5],row,ans=0,junk[5];
    scanf("%i",&t);
    for(int x=1;x<=t;x++)
    {
        ans=0;
        scanf("%i",&row);
        //printf("row1 = %i",row);
        for(int a=1;a<=4;a++)
        {
            if(row!=a)
            {
                for(int b=0;b<4;b++)
                {
                    scanf("%i",&junk[b]);
                    //printf("%i",save1[b]);
                }  
            }
            if(row==a)
            {
                for(int b=0;b<4;b++)
                {
                    scanf("%i",&save1[b]);
                    //printf("%i",save1[b]);
                }
            }
        }
        scanf("%i",&row);
        //printf("row2 = %i",row);
        for(int aa=1;aa<=4;aa++)
        {
            if(row!=aa)
            {
                for(int b=0;b<4;b++)
                {
                    scanf("%i",&junk[b]);
                    //printf("%i",save1[b]);
                }  
            }
            if(row==aa)
            {
                for(int b=0;b<4;b++)
                {
                    scanf("%i",&save2[b]);
                    //printf("%i",save2[b]);
                }
            }
        }
        for(int c=0;c<4;c++)
        {
            for(int d=0;d<4;d++)
            {
                if(save1[c]==save2[d] && ans==0)
                {
                    ans=save1[c];
                }
                else if(save1[c]==save2[d] && ans!=0)
                {
                    ans=100;
                    break;
                }
            }
        }
        if(ans==0)
        {
            printf("Case #%i: Volunteer cheated!\n",x);
            
        }
        else if(ans==100)
        {
            printf("Case #%i: Bad magician!\n",x);
        }
        else if(ans>0 && ans<17)
        {
            printf("Case #%i: %i\n",x,ans);
        }
    }
}
