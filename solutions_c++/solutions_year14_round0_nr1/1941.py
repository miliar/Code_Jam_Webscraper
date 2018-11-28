#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string.h>
#include<cstdlib>

using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


int min(int a,int b)
{
        return a<b?a:b;
}


int max(int a,int b)
{
        return a>b?a:b;
}

int main()
{
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\a.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\b.out","w",stdout);
        int t,i,j,n,m,k,a,b,p;
        int ar[10][10];
        int br[10][10];
        scanf("%d",&t);
        k=t;
        while(t--)
        {
                scanf("%d",&a);
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                scanf("%d",&ar[i][j]);
                        }
                }
                scanf("%d",&b);
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                scanf("%d",&br[i][j]);
                        }
                }
                int f=0,ans;
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                if(ar[a-1][i]==br[b-1][j])
                                       {
                                               f++;
                                               ans=ar[a-1][i];
                                       }

                        }
                }
                if(f==1)
                        printf("Case #%d: %d\n",k-t,ans);
                else if(f==0)
                        printf("Case #%d: Volunteer cheated!\n",k-t);
                else
                        printf("Case #%d: Bad magician!\n",k-t);
        }
        return 0;
}
