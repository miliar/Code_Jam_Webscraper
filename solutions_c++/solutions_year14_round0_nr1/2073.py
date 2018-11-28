#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cases,t,r1,r2,A[17],B[17];
    int i,j,index,count,num;
    scanf("%d",&t);
    cases=0;
    while(cases++ < t)
    {
              scanf("%d",&r1);

              for(i=1;i<=4;i++)
              {
                 for(j=0;j<4;j++)
                 {
                     scanf("%d",&num);
                     A[num]=i;
                 }
              }
              
              scanf("%d",&r2);

              for(i=1;i<=4;i++)
              {
                 for(j=0;j<4;j++)
                 {
                     scanf("%d",&num);
                     B[num]=i;
                 }
              }
              count=0;
              for(i=1;i<=16;i++)
              {
                 if(A[i]==r1 && B[i]==r2)
                 {
                       count++;
                       index=i;
                 }
              }
              if(count==0)
                 printf("Case #%d: Volunteer cheated!\n",cases);
              else if(count==1)
                 printf("Case #%d: %d\n",cases,index);
              else
                 printf("Case #%d: Bad magician!\n",cases);
    }
    return 0;
}
