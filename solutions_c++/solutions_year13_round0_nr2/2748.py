using namespace std;
#include<iostream>
#include<string>
#include<cstring>
int main()
{
int test,x,m,i,j,k,max1,n,flag;
int no[110][110],dp[110][110];
freopen("B-small-attempt0.in","r",stdin);
freopen("output_b.txt","w",stdout);
scanf("%d",&test);
x=1;
while(test--)
{
scanf("%d %d",&n,&m);
printf("Case #%d: ",x);
for(i=0;i<n;i++)
for(j=0;j<m;j++)
scanf("%d",&no[i][j]);
//memset(dp, -1, sizeof(dp[0][0]) * n * m);
for(i=0;i<n;i++)
for(j=0;j<m;j++)
dp[i][j]=-1;
flag=1;
for(i=0;i<n;i++)
{
max1=0;
for(j=0;j<m;j++)
max1=max(no[i][j],max1);
for(j=0;j<m;j++)
{
if(dp[i][j]==-1)
{
if(max1!=no[i][j])
{
for(k=0;k<n;k++)
{
if(dp[k][j]==-1)
dp[k][j]=no[i][j];
else if(dp[k][j]!=no[i][j])
flag=0;
}
}
else
dp[i][j]=no[i][j];   
}
else
if(dp[i][j]!=no[i][j])
flag=0;                             
}
}
if(flag)
printf("YES\n");
else
printf("NO\n");
x++;
}
return 0;
}
