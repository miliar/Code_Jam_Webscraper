#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t,a[10005],left,right,n,m,nub;
int main()
{
     freopen("aa.in","r",stdin);
     freopen("aa.out","w",stdout);
     scanf("%d",&t);
     for(int rr=1;rr<=t;rr++)
     {
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
        {
                nub=0;
                scanf("%d",&a[i]);
                }
                sort(&a[0],&a[n]);
                left = 0;
                right = n-1;
                while(left<=right)
                {
                        if(right!=left && a[left]+a[right]<=m)
                        {
                                left++;
                        }
                        right--;
                        nub++;
                }
                                
     
          printf("Case #%d: %d\n",rr,nub);
     }
     //system("pause");
}
