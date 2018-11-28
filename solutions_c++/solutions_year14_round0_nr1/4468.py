#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#define rep(i,j,n) for(int i=j;i<n;i++)
#define repd(i,j,n) for(int i=j;i>n;i--)
#define N 5
using namespace std;
bool a[20];
int main()
{
    //freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);

    int T,m,b;
    scanf("%d",&T);
    int test=1;
    while(T--)
    {
        scanf("%d",&m);
        memset(a,false,sizeof(a));
        int num=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                 {
                     scanf("%d",&b);
                     if(i==m-1)
                        a[b]=true;
                 }
        }
        int ans=-1;
        scanf("%d",&m);

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
        {
              scanf("%d",&b);
              if(i==m-1&&a[b])
              {
                  num++;
                  ans=b;
              }
        }

        printf("Case #%d: ",test++);
        if(num==1)
            printf("%d\n",ans);
        else if(num>=2)
            printf("Bad magician!\n");
        else if(num==0)
            printf("Volunteer cheated!\n");

    }
    return 0;
}
