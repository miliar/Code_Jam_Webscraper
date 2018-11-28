#include<iostream>
#include<cstdio>
#include<stdlib.h>

using namespace std;
int cmp(const void *x, const void *y)
{
  double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}
int main()
{ int i,k,j,cnt,ans,n,tst,t,ans1,cnt1,start,last;
  double a[1010],b[1010];
 freopen("D-large.in", "r", stdin);
 freopen("outsmall0.txt", "w", stdout);
  scanf("%d",&tst);
  for(t=1;t<=tst;t++)
 {
     scanf("%d",&n);
     for(i=0;i<n;i++)
     scanf("%lf",&a[i]);
     for(i=0;i<n;i++)
     scanf("%lf",&b[i]);
     qsort(a,n,sizeof(double),cmp);
     qsort(b,n,sizeof(double),cmp);

     j=cnt=0;
    for(i=0;i<n;i++)
    {
        if(j>=n)
        break;
        else if(b[j]>a[i])
        {
            cnt++;
            j++;
        }
        else
        {
            while(j<n&&b[j]<a[i])
            {
                j++;
            }
            if(j<n&&b[j]>a[i])
            {
                cnt++;
                j++;
            }
        }
    }
/*cout<<"\n\n";
    for(i=0;i<n;i++)
    cout<<a[i]<<" ";
    cout<<"\n\n";
    for(i=0;i<n;i++)
    cout<<b[i]<<" ";
    cout<<"\n\n";*/
    ans=n-cnt;
   start=0;last=n-1; j=n-1; cnt1=0;
   for(;;)
   {
       if((start>last)||j<0||last<0)
       break;
       if(a[last]>b[j])
       {
           j--;
           last--;
       }
       else
       { //cout<<"yes a[last]:"<<a[last];
           start++;
           j--;
           cnt1++;
       }
   }
   ans1=n-cnt1;
     printf("Case #%d: %d %d\n",t,ans1,ans);
 }
    return 0;
}
