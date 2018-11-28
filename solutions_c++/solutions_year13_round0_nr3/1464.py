#include<iostream>
#include<cstdio>
#include<climits>
#include<utility>
#include<vector>
#include<map>
#include<stack>
#include<deque>
#include<queue>
#include<set>
#include<map>
#include<list>
#include<bitset>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<fstream>
using namespace std;
#define REP(i,a,b) for(long long int i=a;i<b;i++)
#define R return
inline void INPUT(long long int *a){
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}
inline void INPUT(int *a){
register char c=0;
while (c<33) c=getchar_unlocked();
*a=0;
while (c>33)
{
*a=*a*10+c-'0';
c=getchar_unlocked();
}
}
inline void SWAP(int &a, int &b){
a=b+a-(b=a);
}

/* Code from here
Author : Vedavyas Chigurupati
IIIT - Allahabad
*/

int main(){
long long int i,j,k,n,t,m,x,y;
n=39;
long long int arr[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
cin>>t;
k=0;
while(t--){
int ctx=0,cty=0;
k++;
cin>>x>>y;
REP(i,0,39){
if(arr[i]<x) ctx++;
if(arr[i]<=y) cty++;
}
cout<<"Case #"<<k<<": "<<cty-ctx<<endl;
}
R 0;
}

