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
int t,i,n;
long long a,b;
set<long long> s;
typeof(s.begin()) it1,it2;
long long arr[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
s.insert(arr,arr+39);
scanf("%d",&t);
for(i=1;i<=t;++i){
n=0;
scanf("%lld %lld",&a,&b);
it1=s.lower_bound(a);
it2=s.upper_bound(b);
if(it1==it2)
printf("Case #%d: 0\n",i);
else{
it2--;
while(it1!=it2){
it1++;
n++;
}
n++;
printf("Case #%d: %d\n",i,n);
}
}
return 0;
}