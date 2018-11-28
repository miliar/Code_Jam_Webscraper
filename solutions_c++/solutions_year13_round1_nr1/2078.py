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
int i,j,n;
long long r,t,rings;
double ans,temp;
scanf("%d",&n);
for(i=0;i<n;++i){
scanf("%lld %lld",&r,&t);
temp=r; 
ans=(sqrt(8*t+(2*temp-1)*(2*temp-1))+1-2*temp)/4;
rings=(long long int)(floor(ans));
cout<<"Case #"<<i+1<<": "<<rings<<endl;
}
return 0;
}