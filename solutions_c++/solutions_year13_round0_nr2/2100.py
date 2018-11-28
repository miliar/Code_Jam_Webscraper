#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
using namespace std;
 
/*
int input()
{
int t=0;
char c;
c=getchar_unlocked();
while(c<'0' || c>'9')
c=getchar_unlocked();
while(c>='0' && c<='9')
{
t=t*10+c-'0';
c=getchar_unlocked();
}
return(t);
}
*/
 
int main(){
int t,i,j,n,m,k,flag;
int lawn[10][10];
scanf("%d",&t);
for(i=1;i<=t;++i){
flag=1;
int cr[10]={0},cc[10]={0};
scanf("%d %d",&n,&m);
for(j=0;j<n;++j){
for(k=0;k<m;++k){
scanf("%d",&lawn[j][k]);
if(lawn[j][k]==1)
cr[j]++;
}
}
for(j=0;j<m;++j){
for(k=0;k<n;++k){
if(lawn[k][j]==1)
cc[j]++;
}
}
for(j=0;j<n;++j){
if(cr[j]!=m && cr[j]!=0){
for(k=0;k<m;++k){
if(lawn[j][k]==1 && cc[k]!=n){
flag=0;
break;
}
}
}
}
if(flag)
printf("Case #%d: YES\n",i);
else
printf("Case #%d: NO\n",i);
}
return 0;
}