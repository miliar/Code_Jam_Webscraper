#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("small.in","w",stdout);
    char a[1005],b[4050];
    int t,l;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
       scanf("%s",a);
        int i,j,k,n=strlen(a);
        char c1,c2;
        c1=c2=a[0];
        k=j=n/2+1;
        b[j]=c1;
        for(i=1;i<n;i++)
        {
            if(a[i]<c1)
            {
                b[j+1]=a[i];
                j++;
                c2=a[i];
            }
            else
            if(a[i]>=c1)
            {
               b[k-1]=a[i];
               k--;
               c1=a[i];
            }
        }
        printf("Case #%d: ",l);
        for(i=k;i<=j;i++)
             cout<<b[i];
        cout<<endl;
    }
    return 0;
}
