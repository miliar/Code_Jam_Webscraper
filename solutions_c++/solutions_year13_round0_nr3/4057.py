#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
 
using namespace std;
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp make_pair
#define go(i,n) for(int i=0;i<n;i++)
#define go3(i,j,n) for(int i=j;i<n;i++)


bool isPalin(ll n){

  string ret="";
  
  while(n){
    ret+=(n%10)+'0';
    n/=10;
  }

  for(int i=0;i+i<ret.size();i++){
   if(ret[i]!=ret[ret.size()-1-i])
    return false;
  }

  return 1;
}

void oku(){

 ll m[]={1ll,4ll,9ll,121ll,484ll,10201ll,12321ll,14641ll,40804ll,44944ll,1002001ll,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};

 /*for(ll i=0;i<=10000000;i++) {
   if(isPalin(i) && isPalin(i*i)) cout<<i*i<<"ll,";
 }*/

 int T;
 scanf("%d",&T);
 ll A,B;

 go(cs,T){
  scanf("%I64d%I64d",&A,&B);

  int ans=0;

  for(int i=0;i<39;i++)
  if(A<=m[i] && m[i]<=B) ans++;


  printf("Case #%d: %d\n",cs+1,ans);
 
 }




}


int main(){
#ifndef ONLINE_JUDGE
freopen("in","r",stdin);
#endif

oku();

return 0;}