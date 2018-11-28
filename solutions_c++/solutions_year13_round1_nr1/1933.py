/* Author :Anujendra
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>
#define MAX 100000
using namespace std;
int main()

{
unsigned long long circle,num,sum,temp,inner,rt,T,tc,t,i,j,k,l,m,n,o,p,q,r,u,v,x,y,z;
unsigned long long count,flag,result;
//unsigned long long A[1000],B[1000],C[1000],arr[1000];
//unsigned long long AA[1000][1000],BB[1000][1000],CC[1000][1000];

cin>>T;

for(tc=0;tc<T;tc++){


cin>>r>>t;
//inner = r*r;

rt=r;
sum=0;
temp=0;
circle=0;

while (temp<t || temp==t){

if (temp==0)
num=(rt+1)*(rt+1) - rt*rt;
else
num=num+4;

sum = sum + num;

temp=sum;
circle++;
rt++;

}


if (temp>t || circle !=1)
circle--;


cout<<"Case #"<<tc+1<<": "<<circle<<"\n";
}
return 0;
}
