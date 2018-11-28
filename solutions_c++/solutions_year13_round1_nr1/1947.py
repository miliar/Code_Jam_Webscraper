/*
    shubham_1286
   algo =             */

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
using namespace std;
int main()
{
     freopen("c:\\users\\shubham\\desktop\\aa.txt","r",stdin);
     freopen("c:\\users\\shubham\\desktop\\out.txt","w",stdout);
int m;
cin>>m;
int test=1;
while(test<=m)
{
unsigned long long r,t,sum=0,coun=0;
scanf("%llu%llu",&r,&t);
while(1)
{
sum+=(r+(r+1));
r=r+2;
//cout<<sum<<endl;
if(sum<=t)
coun++;
else
break;
}
printf("Case #%d: %llu\n",test,coun);
test++;
}


}
