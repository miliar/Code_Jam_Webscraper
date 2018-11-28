#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>

#define il(n) scanf("%lld",&n)
#define i(n) scanf("%d",&n)

using namespace std;
double arr[100005][3];
int main()
{
int tc,j;
cin>>tc;
for(j=1;j<=tc;j++)
{
double c,f,x,miny;
int i,maxy;
scanf("%lf%lf%lf",&c,&f,&x);
arr[0][0]=(x/2.0);
arr[0][1]=2.0;
miny=arr[0][0];
maxy=x/c;
for(i=1;i<=maxy;i++)
{
    arr[i][1]=arr[i-1][1]+f;
    arr[i][0]=arr[i-1][0]+(c/arr[i-1][1])+(x/arr[i][1])-(x/arr[i-1][1]);
   // printf("%0.8lf\n",arr[i][0]);
    if(arr[i][0]<miny)
        miny=arr[i][0];
}
printf("Case #%d: %0.7lf\n",j,miny);
}
return 0;
}
