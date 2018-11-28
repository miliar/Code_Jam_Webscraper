#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int s1,s2,e1,e2;

int check (double A[1000],double B[1000])
{
	int i1,i2;
    i1=s1;i2=s2;
    for(;i1<e1;i1++,i2++)
    {
        if(A[i1]<B[i2])
        {
           s1++;
           e2--;
           return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("outputDlarge.txt","w",stdout);
    
    int t,n,cases,i,j,ans1,ans2;
    double wt,A[1000],B[1000];
    scanf("%d",&t);
    cases=0;
    while(cases++ < t)
    {
              scanf("%d",&n);
              s1=0;s2=0;
              e1=n;e2=n;
              for(i=0;i<n;i++)
              {
                  scanf("%lf",&wt);
                  A[i]=wt;
              }
              for(i=0;i<n;i++)
              {
                  scanf("%lf",&wt);
                  B[i]=wt;
              }
              sort(A,A+n);
              sort(B,B+n);
              while(check(A,B)==0);
              ans1=e1-s1;
              
              s1=0;s2=0;
              e1=n;e2=n;
              ans2=0;
              for(i=0;i<n;i++)
              {
              	  e1--;
                  e2--;
                  if(A[e1]>B[e2])
                  {
                      ans2++;
                      e2++;
                  }
              }

              printf("Case #%d: %d %d\n",cases,ans1,ans2);
    }

    return 0;
}
