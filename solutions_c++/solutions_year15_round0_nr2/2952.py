#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <math.h>
using namespace std;
///CODEJAMM
#define MAXP 1001
int minb[MAXP][MAXP];
int T,D;
int P[MAXP];

int main()
{
freopen("B-large.in","r",stdin);
freopen("bre.out","w",stdout);

 ///PRECOMPUTE minb[x][k] minimalni broj deljenja x, tako da imamo <=k brisanja
 for (int i=1;i<=1000;i++)
    for (int j=1;j<=1000;j++)
 {
     minb[i][j]=(i/j+((i%j)?1:0))-1;
 }

cin>>T;
for (int i=0;i<T;i++)
{
    scanf("%d",&D);
    for (int j=0;j<D;j++)
        scanf("%d",&P[j]);
   int sol=MAXP;
   for (int numb=1;numb<=1000;numb++)
   {
       int cursol=numb;
       for (int j=0;j<D;j++)
          cursol+=minb[P[j]][numb];
       if (cursol<sol) sol=cursol;
   }
cout<<"Case #"<<(i+1)<<": "<<sol<<endl;
}
return 0;
}
