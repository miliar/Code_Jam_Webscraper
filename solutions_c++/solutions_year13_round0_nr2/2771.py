#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)

int main()
{   freopen("B-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
int t,co=0;
cin>>t;
while(t--)
{       
co++;
int noss,m,result=1;
cin>>noss>>m;
int arr[noss][m];
for(int pi=0;pi<noss;pi++)
{
for(int jat=0;jat<m;jat++)
{
cin>>arr[pi][jat];
}
}
for(int pi=0;pi<noss;pi++)
{
for(int j=0;j<m;j++)
{if(arr[pi][j]==1)
{
int flag=1;
for(int y=0;y<m;y++)
{if(arr[pi][y]!=arr[pi][j]){flag=0;break;}}
if(flag==0)
{flag=1;for(int y=0;y<noss;y++){if(arr[y][j]!=arr[pi][j]){flag=0;break;}}}
if(flag==0)
{result=0;break;}}}if(result==0)break;

}
cout<<"Case #"<<co<<": ";if(result==0)cout<<"NO"<<endl;else cout<<"YES"<<endl;
}
return 0;
}

