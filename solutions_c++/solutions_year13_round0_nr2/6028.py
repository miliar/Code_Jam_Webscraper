/*
    shubham_1286
   algo = brute            */
using namespace std;
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000007
int main()
{
    freopen("c:\\users\\shubham\\desktop\\p.txt","r",stdin);
    freopen("c:\\users\\shubham\\desktop\\s.txt","w",stdout);
int t,test;
scanf("%d",&t);
test=1;
while(test<=t)
{
int n,m;
scanf("%d%d",&n,&m);
int arr[n+1][m+1],c;
for(int i=0;i<n;i++)
{for(int j=0;j<m;j++)
scanf("%d",&arr[i][j]);}

int flag=10,row=0,col=0;

for(int i=0;i<n;i++)
{
int max=*max_element(&arr[i][0],&arr[i][0]+m);
for(int j=0;j<m;j++)
{
flag=10;row=0;col=0;
//cout<<max<<endl;
if(arr[i][j]<max)
{
//for row part
//cout<<arr[i][j]<<endl;
for(int k=0;k<m;k++)
{
if(arr[i][k]==arr[i][j])
row++;
}
//cout<<"row "<<row<<endl;
//for column
for(int l=0;l<n;l++)
{
if(arr[l][j]==arr[i][j])
col++;
}
//cout<<"col "<<col<<endl;
if(row==m||col==n)
{flag=10;}
else
{
flag=2;
break;
}

}//if ends here
}//inner for ends
if(flag==2)
break;
}//outer foor loop ends
if(flag==2)
printf("Case #%d: NO\n",test);
else
printf("Case #%d: YES\n",test);
test++;
}}
