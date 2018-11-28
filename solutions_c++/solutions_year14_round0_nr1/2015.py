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
        int t1,i,j,x,y,n,m,k1,a,b,p;
        int arr[10][10];
        int brr[10][10];
        scanf("%d",&t1);
        k1=t1;
        while(t1--)
        {
                scanf("%d",&a);
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                scanf("%d",&arr[i][j]);
                        }
                }
                scanf("%d",&b);
                for(i=0;i<4;i++)
                {
                        for(j=0;j<4;j++)
                        {
                                scanf("%d",&brr[i][j]);
                        }
                }
                int ctr=0;
                int an;
        for(i=0;i<4;i++)
                {
        for(j=0;j<4;j++)
                {
                        if(arr[a-1][i]==brr[b-1][j])
                                       {
                                               ctr++;
                                               an=arr[a-1][i];
                                       }

                        }
                }
        if(ctr==1)
        printf("Case #%d: %d\n",k1-t1,an);
                else if(ctr==0)
                printf("Case #%d: Volunteer cheated!\n",k1-t1);
        else
                printf("Case #%d: Bad magician!\n",k1-t1);
        }
        return 0;
}
