#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
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
#include<stdio.h>



#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(long int i=a;i<b;i++)
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
long long int SI(string str) {long long int ans; stringstream s; s<<str; s>>ans; return ans;}
string IS(long long int n) {string str; stringstream s; s<<n; s>>str; return str;}

ULL arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001ULL,10221412201ULL,12102420121ULL,12345654321ULL,40000800004ULL,1000002000001ULL,1002003002001ULL,1004006004001ULL,1020304030201ULL,1022325232201ULL,1024348434201ULL,1210024200121ULL,1212225222121ULL,1214428244121ULL,1232346432321ULL,1234567654321ULL,4000008000004ULL,4004009004004ULL};

int main()
{
   freopen("read.txt","r",stdin);
   freopen("write.txt","w",stdout);

  long long int t,a,b;
  cin>>t;
  FOR(j,1,t+1)
  {
      long int count=0;
      cin>>a>>b;
      long long int i;
      for(int i=0;i<39;i++)
      {
         if(a<=arr[i]&&b>=arr[i]) count++;
      }
    cout<<"Case #"<<j<<": "<<count<<"\n";
  }
  return 0;
}
