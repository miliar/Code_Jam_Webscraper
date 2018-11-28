#include<stdio.h>
#include<stdlib.h>

int cmp(const void * a,const void * b)
{
    double * xx=(double *)a;
    double * yy=(double *)b;

    if(*xx>*yy)
      return 1;
    if(*xx<*yy)
      return -1;
    return 0;
}

int main()
{

    //freopen("inp4.in","r+",stdin);
    //freopen("out4.out","w+",stdout);


    freopen("ques42.in","r+",stdin);
    freopen("out42.out","w+",stdout);


    int t;
    scanf("%d",&t);

    int k=0;
    while(t--)
     {
         k++;

         int n;
         scanf("%d",&n);

         double aa[1009]={0.0};
         double bb[1009]={0.0};

         int i;
         for(i=0;i<n;i++)
           scanf("%lf",&aa[i]);

         for(i=0;i<n;i++)
           scanf("%lf",&bb[i]);

         qsort(aa,n,sizeof(aa[0]),cmp);
         qsort(bb,n,sizeof(bb[0]),cmp);

/*
         printf("\n");
         for(i=0;i<n;i++)
           printf("%.5lf ",aa[i]);
         printf("\n");

         printf("\n");
         for(i=0;i<n;i++)
           printf("%.5lf ",bb[i]);
         printf("\n");
*/

         int cnt1=0;
         int va1[1009]={0};
         int vb1[1009]={0};

         for(i=n-1;i>=0;i--)
           {
               if(va1[i]==1)
                 continue;

               double xx=aa[i];

               int ind;
               int j;
               for(j=n-1;j>=0;j--)
                 if(vb1[j]==0)
                   {
                       ind=j;
                       break;
                   }

               if(xx<bb[ind])
                  {
                     for(j=0;j<n;j++)
                       {
                           if(va1[j]==0)
                             break;
                       }

                     va1[j]=1;

                     double zz=aa[j];

                     int f1=0;

                     for(j=n-1;j>=0;j--)
                       {
                           if(vb1[j]==0 && bb[j]>zz)
                            {
                                f1=1;
                                vb1[j]=1;
                                break;
                            }

                       }



                     i++;
                  }
               else
                  {
                     va1[i]=1;

                     int f1=0;
                     int j;

                     for(j=n-1;j>=0;j--)
                      {
                         if(vb1[j]==0 && bb[j]>aa[i])
                            {
                                f1=1;
                                vb1[j]=1;
                                break;
                            }
                      }

                     if(f1==0)
                      {
                        cnt1++;

                        for(j=n-1;j>=0;j--)
                            if(vb1[j]==0)
                             {
                                vb1[j]=1;
                                break;
                             }
                     }
                  }
           }


         int va2[1009]={0};
         int vb2[1009]={0};

         int cnt2=0;
         for(i=n-1;i>=0;i--)
           {
               double xx=aa[i];

               int f2=0;
               int j;
               for(j=0;j<n;j++)
                 {
                     if(vb2[j]==0 && bb[j]>aa[i])
                       {
                            f2=1;
                            vb2[j]=1;
                            break;
                       }
                 }

               if(f2==0)
                  {
                      cnt2++;

                      for(j=0;j<n;j++)
                        if(vb2[j]==0)
                          {
                                vb2[j]=1;
                                break;
                          }
                  }
           }

         printf("Case #%d: %d %d\n",k,cnt1,cnt2);
     }
    return 0;
}
