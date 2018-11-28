#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,n,i,j,k,l,m;
    int b[15];
    scanf("%d",&t);
    int z=1;
    while(t--)
    {

        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",z);
            z++;
        }
        else{
        int temp,cnt=0;
        for(i=0;i<10;i++)
            b[i]=0;
        l=n;
        while(l)
        {
            int x=l%10;
            if(b[x]==0)
            {
                b[x]=1;
                cnt++;
            }
            l/=10;
        }
        for(i=2;cnt<10;i++)
        {
           l=n*i;
           m=l;
          while(l)
          {
            int x=l%10;
            l/=10;
            if(b[x]==0)
            {
                b[x]=1;
                cnt++;
            }
          }
            if(cnt==10)
            {
                printf("Case #%d: %d\n",z,m);
            }
        }
        z++;
      }
    }
  return 0;
}

