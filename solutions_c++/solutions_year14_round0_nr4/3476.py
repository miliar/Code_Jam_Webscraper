#include<bits/stdc++.h>
using namespace std;
#define N 1000
double a[N + 10];
double b[N + 10];
int check[N + 10];
int main()
{
    int tc,t;
    freopen("D-large.in","r",stdin);
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++)
    {
        int n,i;
        scanf("%d",&n);
        for(i = 0 ; i<n ; i++)
        scanf("%lf",&a[i]);
        for(i = 0 ; i<n ; i++)
        scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        for(i = 0 ; i<n ; i++)
        check[i] = 0;
        int j;
        int c = 0;
        memset(check,0,sizeof(check));
        for(i = 0 ; i<n ; i++)
        {

            for(j = 0 ; j<n ; j++)
            {
                if(check[j] == 0 && b[j] > a[i])
                {
                    check[j] = 1;
                    c++;
                    break;
                }
            }
        }
        for(i = 0 ; i<n ; i++)
        check[i] = 0;
        c = n - c;
        int p = 0;
        int l = n-1;
        int n1 = 0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            if(check[j]==0)
            {
                if(b[j]<a[i])
                {
                    check[j]=1;
                    n1++;
                }
                else
                {
                    check[l]=1;
                    l--;
                }
                break;
            }
        }
      printf("Case #%d: %d %d\n",t,n1,c);
    }
    return 0;
}
