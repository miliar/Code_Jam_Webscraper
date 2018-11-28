#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t,ans,p,n,a[1005],to_right[1005],to_left[1005],max_now;
int main()
{
     freopen("bb.in","r",stdin);
     freopen("bb.out","w",stdout);
     scanf("%d",&t);
     for(int rr=1;rr<=t;rr++)
     {
                ans=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
                scanf("%d",&a[i]);
                to_left[i]=i;
                to_right[i]=n-1-i;
        }
        for(int i=0;i<n;i++)
        {
                
                max_now = 1000000001;
                for(int j=0;j<n;j++)
                {
                        if(a[j]<max_now)
                        {
                                max_now=a[j];
                                p=j;
                        }
                }
                ans+=min(to_left[p],to_right[p]);
                a[p]=1000000001;
                for(int j=0;j<p;j++)
                {
                        to_right[j]--;
                }
                for(int j=p+1;j<n;j++)
                {
                        to_left[j]--;
                }
        }
          printf("Case #%d: %d\n",rr,ans);
     }
     //system("pause");
}
