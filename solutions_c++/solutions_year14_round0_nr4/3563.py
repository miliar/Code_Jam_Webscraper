#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
int i,n,start1,start2,t,k=0,win1,win2;
scanf("%d",&t);
while(++k <= t)
{
scanf("%d",&n);
vector<double> v1(n),v2(n);
for(i=0;i<n;i++)
 scanf("%lf",&v1[i]);
for(i=0;i<n;i++)
 scanf("%lf",&v2[i]);

/*
for(i=0;i<n;i++)
 printf("%lf ",v1[i]);
printf("\n");
for(i=0;i<n;i++)
 printf("%lf ",v2[i]);

printf("\n");
*/
sort(v1.begin(),v1.end());
sort(v2.begin(),v2.end());
//printf("After sorting\n");

//for(i=0;i<n;i++)
// printf("%lf ",v1[i]);
//printf("\n");

//for(i=0;i<n;i++)
// printf("%lf ",v2[i]);
//printf("\n");
start1=0;
start2=0;
win1=0;
while(start2<n && start1<n)
{
  if(v1[start1] > v2[start2]) { win1++; start2++;}
  else
{
start1++;
start2++;
}
//player2 plays optimally then player 1 will win win1 points
}
start1=0;
start2=0;
win2=0;
while(start2<n && start1<n)
{
  if(v2[start2] > v1[start1]) {win2++; start1++;}
  else
{
start1++;
start2++;
}
//player1 plays optimally then player 2 will win win2 points;
// therefore player1 will win 'n-win2' points this time;
}
printf("Case #%d: %d %d\n",k,n-win2,win1);
}//cases loop :while ends

return 0;
}
