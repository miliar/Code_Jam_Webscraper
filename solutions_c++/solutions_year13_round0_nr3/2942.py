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
#include<cstring>
using namespace std;
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,b) for(int (i)=a;(i)<(b);(i)++)
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define _mp make_pair
#define MOD 1000000007
#define MAXN 200020
bool isPalindrome(long long x) {
  if (x < 0) return false;
  long long div = 1;
  while (x / div >= 10) {
    div *= 10;
  }
  while (x != 0) {
    long long l = x / div;
    long long r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

int main()
{
  //freopen("C.in","r",stdin);
  //freopen("out.txt","w",stdout);
  long long T,n,m,x,number=0;
  cin>>T;
  while(T--){
       cin>>n>>m;
       long long i,cnt=0;
       number++;
       double k=sqrt(n);
       if(ceil(k)==floor(k)){
         i=(long long)k;
       }else{
         i=(long long)k +1;
       }
       //bool isNumPalindrome=false,isRootPalindrome=false,isPerfectSquare=false;
       cout<<"Case #"<<number<<": ";
       for(;i*i<=m;i++){
            if(isPalindrome(i)){
               if(isPalindrome(i*i)){
                 cnt++;
               }
            }
       }
       cout<<cnt<<endl;
  }

  return 0;
}
