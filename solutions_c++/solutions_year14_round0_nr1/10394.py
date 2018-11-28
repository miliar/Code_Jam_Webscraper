#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<fstream>
int main()
{
   std::ifstream in;
   std::ofstream out;
   in.open("a.in");
   out.open("b.out");
    int t;
    //scanf("%d",&t);
    in>>t;
    int a[5][5],b[5][5];
    int c[5],d[5];
    for(int q=1;q<=t;q++)
    {
        int m,n;
       // scanf("%d",&m);
       in>>m;
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
           // scanf("%d",&a[i][j]);
           in>>a[i][j];
        }
        //printf("%\n");
    }

     //scanf("%d",&n);
     in>>n;
     for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            //scanf("%d",&b[i][j]);
            in>>b[i][j];
        }
        //printf("%\n");
    }


    /*for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("%\n");
    }
     for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            printf("%d ",b[i][j]);
        }
        printf("%\n");
    }*/
                /*copying items */
        for(int k=1;k<=4;k++)
        {
            c[k]=a[m][k];
        }
       // printf("\n");

         for(int k=1;k<=4;k++)
        {
            d[k]=b[n][k];
        }
       // printf("\n");

        /*for(int l=1;l<=4;l++)
        {
            printf("%d ",c[l]);
        }
         printf("\n");
            for(int l=1;l<=4;l++)
        {
            printf("%d ",d[l]);
        }*/
        int cnt=0,s;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(c[i]==d[j])
                    {
                        cnt++;
                        s=c[i];
                    }
            }
        }

        if(cnt==1)
            //printf("Case #%d: %d\n",q,s);
            out<<"Case #"<<q<<": "<<s<<"\n";
        else if(cnt>1)
            //printf("Case #%d: %s\n",q,"Bad magician!");
            out<<"Case #"<<q<<": "<<"Bad magician!"<<"\n";
        else if (cnt==0)
            //printf("Case #%d: %s\n",q,"Volunteer cheated!");
            out<<"Case #"<<q<<": "<<"Volunteer cheated!"<<"\n";


    }
    return 0;
}
