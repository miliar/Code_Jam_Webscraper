#include<stdio.h>
int main()
{
    int t,i,j,hash[17],a1,a2,x,count,ans,k=1;
    FILE *fp,*fp1;

    fp = fopen("A-small-attempt3.in","r");
    fp1 = fopen("output","w");
    fscanf(fp , "%d" , &t);

    while(t--)
    {
        count=0;
        fscanf(fp,"%d",&a1);

        for(i=1;i<=16;i++)
          hash[i]=0;


        for(j=1;j<=4;j++)
        {
           for(i=1;i<=4;i++)
           {
              fscanf(fp , "%d" , &x);
              if(j==a1)
              {
                  hash[x]=1;
              }
           }
        }

         fscanf(fp,"%d",&a2);

        for(j=1;j<=4;j++)
        {
           for(i=1;i<=4;i++)
           {
              fscanf(fp , "%d" , &x);
              if(j==a2)
              {
                  if(hash[x]==1)
                  {
                       count++;
                       ans=x;
                  }
              }
           }
        }

        if(count==1)
        {
              fprintf(fp1,"Case #%d: %d\n",k,ans);
        }
        else if(count==0)
        {
              fprintf(fp1,"Case #%d: Volunteer cheated!\n",k);
        }
        else
        {
              fprintf(fp1,"Case #%d: Bad magician!\n",k);
        }
        k++;

    }
    return 0;
}
