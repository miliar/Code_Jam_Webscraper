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

int lcs( char *X, char *Y, int m, int n )
{
   int L[m+1][n+1];
   int i, j;

   /* Following steps build L[m+1][n+1] in bottom up fashion. Note
      that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
   for (i=0; i<=m; i++)
   {
     for (j=0; j<=n; j++)
     {
       if (i == 0 || j == 0)
         L[i][j] = 0;

       else if (X[i-1] == Y[j-1])
         L[i][j] = L[i-1][j-1] + 1;

       else
         L[i][j] = max(L[i-1][j], L[i][j-1]);
     }
   }

   /* L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1] */
   return L[m][n];
}

int main()
{
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\a.in","r",stdin);
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\b.out","w",stdout);
        int t,i,j,m,k,p,c;
        int a,b,k1;
        scanf("%d",&t);
        k1=t;
        while(t--)
        {
                c=0;
                scanf("%d",&a);
                scanf("%d",&b);
                scanf("%d",&k);
                for(i=0;i<a;i++)
                {
                        for(j=0;j<b;j++)
                        {
                                if((i&j)<k)
                                        c++;
                        }
                }
                printf("Case #%d: %d\n",k1-t,c);
        }

        return 0;
}
