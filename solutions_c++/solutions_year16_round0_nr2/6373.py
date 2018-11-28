#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bone.in","w",stdout);
    int t,j;
    char a[105];
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%s",a);
        int i,c=0,n=strlen(a);

        for(i=1;i<n;i++)
            if(a[i]!=a[i-1])
              c++;
        printf("Case #%d: ",j);
        if(a[n-1]=='-')
             printf("%d\n",c+1);
        else
            printf("%d\n",c);
    }
    return 0;
}
