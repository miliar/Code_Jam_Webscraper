#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,x,s=0,q,qq=1,n,c;char a[1110];
    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {c=0;
    s=0;
        scanf("%d",&n);
        scanf("%s",a);
        for(i=0;i<(n+1);i++)
          {
              x=a[i]-'0';
              //cout<<x<<"\n";
              s+=x;
              if(s<(i+1))
                {q=(i+1-s);c+=q;s+=q;}
          }
          printf("Case #%d: %d\n",qq++,c);
        //printf("%d\n",ans);
    }
    return 0;
}
