#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char a[1005];
int main()
{
    ll t,n,p,i,j,r,c=1,l,k;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%s",&a);
        printf("Case #%lld: ",c++);
        ll ans=0;
        n=strlen(a);
        for(i=n-1;i>=0;i--)
        {
            if(a[i]=='+')
            continue;
            else
            {
                for(j=0;j<i;j++)
                {
                    if(a[j]=='-')
                    break;
                }
                if(j>0)
                {
                   // printf("J:%d\n",j);
                    //swap(0,j-1);
                    l=0;
                    r=j-1;
                    while(l<r)
                    {
                        char temp=a[l];
                        a[l]=a[r];
                        a[r]=temp;

                        l++;
                        r--;
                    }
                    for(k=0;k<=j-1;k++)
                    {
                        if(a[k]=='+')
                        a[k]='-';
                        else
                        a[k]='+';

                    }
                  //  printf("%s\n",a);
                    ans++;
                }
                //swap(0,i);
                l=0;
                r=i;

                while(l<r)
                {
                    char temp=a[l];
                    a[l]=a[r];
                    a[r]=temp;

                    l++;
                    r--;
                }
                for(k=0;k<=i;k++)
                {
                    if(a[k]=='+')
                    a[k]='-';
                    else
                    a[k]='+';

                }
               // printf("%s\n",a);
                ans++;
            }
        }
        printf("%lld\n",ans);
    }
    return 0;
}
