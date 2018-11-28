#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <limits>

using namespace std;

#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define REP(I,N) FOR(I,0,N)
#define LL long long
#define S(N) scanf("%d", &N)
#define SL(N) scanf("%lld", &N)
#define PB push_back
#define MP make_pair
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define cell pair<int,int>
#define edge pair<int, cell>
#define clear(x) memset(x,0,sizeof(x))
#define CHECK_BIT(var,pos) ((var) & (1<<(pos))

typedef vector<int> vi;
typedef vector<LL> vii;
cell dir[4]={cell(0,1), cell(1,0), cell(0,-1), cell(-1,0) };
/*bool chkpalin(LL num)
{
     LL n, rev, dig;
     n = num;
     rev = 0;
     while (num > 0)
     {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
      }
      return (n == rev ? true : false);
}*/
string arr[39] = { "1","4","9","121","484","10201","12321","14641","40804","44944","1002001",
"1234321","4008004","100020001","102030201","104060401","121242121","123454321","125686521",
"400080004","404090404","10000200001","10221412201","12102420121","12345654321","40000800004",
"1000002000001","1002003002001","1004006004001","1020304030201","1022325232201","1024348434201",
"1210024200121","1212225222121","1214428244121","1232346432321","1234567654321","4000008000004","4004009004004"};
LL calc( string s)
{
         LL num = 0;
         for(int i=0; i<s.length(); i++)
         num = num*10 + (s[i]-'0') ;
         return num;
}
int main()
{
    //freopen("C-large-1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t, ctr = 0; 
    S(t);
    while(t--)
    {
              LL  cnt =0, i, j;
              LL a, b;
              SL(a) ; SL(b);
              for( i = 0; i<39 ; i++)
              {
                   LL tmp = calc( arr[i] );
                   if( tmp>=a && tmp<=b)
                   cnt++;
              } 
              printf("Case #%d: %d\n", ++ctr, cnt);
    }
    return 0;
}
