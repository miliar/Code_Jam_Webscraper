#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("out.txt","w",stdout);
        int c,a,b,n,i,j,k,p,q,input[100],input1[100],count=0,m,val,l;
        scanf("%d",&l);
        for(i=1;i<=l;i++)
        {

            scanf("%d",&p);
            for(j=1;j<=16;j++)
            {
                scanf("%d",&input[j]);
            }
            scanf("%d",&q);
             for(k=1;k<=16;k++)
            {
                scanf("%d",&input1[k]);
            }
            b=(p-1)*4+1;
            c=(q-1)*4+1;
            p=p*4;
            q=q*4;

            for(m=b;m<=p;m++)
            {
                for(j=c;j<=q;j++)
                {
                 //   printf("%d %d\n",input[m],input1[j]);
                    if(input[m]==input1[j])
                    {
                        val=input[m];
                        count++;
                    }
                }
            }
            if(count==0)
            {
                printf("Case #%d: Volunteer cheated!\n",i);
                 count=0;
            }
            else if(count==1)
            {
                printf("Case #%d: %d\n",i,val);
                 count=0;
            }
            else
            {
                printf("Case #%d: Bad magician!\n",i);
                 count=0;
            }
            count=0;

        }

}
/*
3
2
1 2 3 4 5 6 7  8 9 10 11 12 13 14 15 16
3
1 2 5 4 3 11 6 15 9 10 7 12 13 14 8 16*/
