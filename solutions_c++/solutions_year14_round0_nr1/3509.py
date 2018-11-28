#include<stdio.h>
#include<string.h>
int hash[17]={0};
int main()
{

    int t;
     freopen( "A-small-attempt2.in", "r", stdin);
    scanf("%d",&t);
    int te=1;
    while(te<=t)
    {
        int a[4][4];
        memset(hash,0,sizeof(hash));
        int ans1,ans2;
        scanf("%d",&ans1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
               {
                   scanf("%d",&a[i][j]);
                   if(ans1==i+1)
                   {
                       hash[a[i][j]]=1;


                   }
               }

        scanf("%d",&ans2);

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
               {
                   scanf("%d",&a[i][j]);
                   if(ans2==i+1)
                   {
                       hash[a[i][j]]=hash[a[i][j]]+1;;
                   }

               }



        int count=0,save;
        for(int i=1;i<17;i++)
        {
            if(hash[i]==2)
            {  count++;
               save=i;
            }


        }

        if(count==1)
            printf("Case #%d: %d\n",te,save);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",te);
        else
            printf("Case #%d: Bad magician!\n",te);


        te++;




}
}
