#include<stdio.h>
#include<algorithm>

bool mcomp(long double i,long double j)
{

    return (i<j);
}

int main()
{
    int t,te=1;
    long double a[1001],b[1001],aa[1001],bb[1001];
    freopen("D-large.in","r",stdin);
    scanf("%d",&t);
    while(te<=t)
    {
       int n;
       int i,j;
      scanf("%d",&n);
      for(i=0;i<n;i++)
            scanf("%Lf",&a[i]);
      for(i=0;i<n;i++)
            scanf("%Lf",&b[i]);

      int count=0,count1=0;
      std::sort(a,a+n,mcomp);
      std::sort(b,b+n,mcomp);


    for(i=0;i<n;i++)
       aa[i]=a[i];



    for(i=0;i<n;i++)
        bb[i]=b[i];



    for(i=0,j=0;i<n&&j<n;)
    {

            if(a[i]<b[j])
            {
                i++;
                j++;
                count++;
            }
            else
            {
                j++;
            }


    }

    int k=0;
    for(i=n-1,j=n-1;i>=0&&j>=0;)
    {


          if(bb[j]!=-1&&aa[i]!=-1&&aa[i]>bb[j])
          {
              bb[j]=-1;
              aa[i]=-1;
              i--;
              j--;

          }

          else if(aa[i]<bb[j])
          {
            aa[k]=-1;
            bb[j]=-1;
            k++;
            j--;
            count1++;

          }
          else
          {
              i--;
              j--;
          }

    }










    printf("Case #%d: %d %d\n",te,n-count1,n-count);
    te++;


    }





}
