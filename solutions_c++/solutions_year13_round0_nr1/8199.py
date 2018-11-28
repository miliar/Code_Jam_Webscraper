#include<stdio.h>
#include<iostream>
using namespace std;


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("trialop","w",stdout);
    int p,t;
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        int i,j;
        char B[4][4];
        int A[4][4];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>B[i][j];
                A[i][j]=44;
            }
        }


        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(B[i][j]=='X')A[i][j]=1;
                else if(B[i][j]=='O')A[i][j]=0;
                else if(B[i][j]=='T')A[i][j]=2;
                else if(B[i][j]=='.')A[i][j]=3;
            }
        }
        int cc,co=0,won=0;
        //check row win
        for(i=0;i<4;i++)
        {

            if(A[i][0]<2)
            {
                int cr=1;
                int test = A[i][0];
                for(j=1;j<4;j++)
                {
                    if(A[i][j]==2)
                        cr++;
                    else if((A[i][j]<2)&&(A[i][j]==test))
                        cr++;

                }
                if(cr==4)
                    {printf("Case #%d: %c won\n",p,B[i][0]);won++;}
            }
            else if(A[i][0]==2)
            {
                int cr=1;
                int test=A[i][1];
                if(test<2)cr++;
                for(j=2;j<4;j++)
                {
                    if((A[i][j]<2)&&(A[i][j]==test))
                        cr++;


                }
                if(cr==4)
                    {
                        printf("Case #%d: %c won\n",p,B[i][1]);
                        won++;

                    }
            }
        }

        //each column
        if(won==0){
        for(i=0;i<4;i++)
        {

            if(A[0][i]<2)
            {
                int cc=1;
                int test = A[0][i];
                for(j=1;j<4;j++)
                {
                    if(A[j][i]==2)
                        cc++;
                    else if((A[j][i]<2)&&(A[j][i]==test))
                        cc++;

                }
                if(cc==4)
                    {printf("Case #%d: %c won\n",p,B[0][i]);won++;}
            }
            else if(A[0][i]==2)
            {
                int cc=1;
                int test=A[1][i];
                if(test<2)cc++;
                for(j=2;j<4;j++)
                {
                    if((A[j][i]<2)&&(A[j][i]==test))
                        cc++;

                }
                if(cc==4)
                    {printf("Case #%d: %c\n",p,B[1][i]);won++;}
            }
        }

        }

        //each diagnol
        //L-R

        int test1=A[0][0],test2=A[0][3],cd1=1,cd2=1;
        if((won==0)&&(test1<3))
        {
        for(i=1;i<4;i++)
        {
            if(test1==2)
                {
                    test1=A[i][i];
                    if(test1<2)
                        cd1++;
                }
            else if((A[i][i]==test1)||(A[i][i]==2))
                    cd1++;
        }
        if(cd1==4)
        {
            printf("Case #%d: %c won\n",p,B[0][0]);
            won++;
        }
        }
        //R-L
        if((won==0)&&(test2<3))
        {
        for(i=1;i<4;i++)
        {
            if(test2==2)
                {
                    test2=A[i][3-i];
                    if(test1<2)
                        cd2++;
                }
            else if((A[i][3-i]==test2)||(A[i][3-i]==2))
                    cd2++;
        }
        if(cd2==4)
            {
                printf("Case #%d: %c won\n",p,B[0][3]);
                won++;
            }
        }

        if(won==0)
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                    if(A[i][j]==3)
                        {co=1;break;}
            }
        }
        if(co==1)
            printf("Case #%d: Game has not completed\n",p);
        if((co==0)&&(won==0))
        {
            printf("Case #%d: Draw\n",p);

        }


    }
    return 0;
}
