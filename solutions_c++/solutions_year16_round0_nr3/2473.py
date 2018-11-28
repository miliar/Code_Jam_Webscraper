#include<cstdio>
#include<set>
#include<map>
#include<iostream>
#include<queue>
#include<stack>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<ctime>
#define read freopen("in.txt","r",stdin)
#define maxlongint 2147483647
typedef  long long LL;
typedef  unsigned long long ULL;
#define fori for(i=1;i<=n;i++)
#define forj for(j=1;j<=m;j++)
#define FOR(i,n) for(i=1;i<=n;i++)
#define REP(i,a,b) for(i=a;i<=b;i++)
#define DREP(i,a,b) for(i=a;i>=b;i--)
#define DOWN(i,n) for(i=n;i>=1;i--)
#define enter cout<<endl;
#define in push_back
#define out pop_back
#define ll long long
#define lson 2*k
#define rson 2*k+1
#define left l,mid,lson
#define offcin ios::sync_with_stdio(false)
#define right mid+1,r,rson
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sd(x,y) scanf("%d%d",&x,&y)
#define sch(s) scanf("%s",s)
#define fillfalse(v) memset(v,false,sizeof(v))
#define filltrue(v) memset(v,true,sizeof(v))
#define Fill0(a)    memset(a,0,sizeof(a))
#define Fillplus(a)    memset(a,-1,sizeof(a))
#define lowbit(x) x&(-x)
using namespace std;
string ss;
int n,k,i,j,l,x,y,ans;
LL sd;
int a[20];
int main()
{
freopen("C-small-attempt1.in","r",stdin);
freopen("out.txt","w",stdout);
  int ii,TT;
  cin>>TT;
  FOR(ii,TT)
  {
   cin>>x>>y;
cout<<"Case #1:"<<endl;
cout<<"1000000000000001 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000000000101 13 11 3 4751 173 3 53 109 3"<<endl;
cout<<"1000000000000111 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000000001001 73 5 3 19 19 3 5 19 3"<<endl;
cout<<"1000000000001101 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000000010011 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000000011001 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000000011011 5 1567 15559 6197 5 5 1031 7 83"<<endl;
cout<<"1000000000011111 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000000100101 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000000101011 3 7 13 3 5 43 3 73 7"<<endl;
cout<<"1000000000101111 5 2 3 2 37 2 5 2 3"<<endl;
cout<<"1000000000110001 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000000110101 23 17 11 23 5 299699 43 239 59"<<endl;
cout<<"1000000000110111 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000000111011 17 2 3 2 73 2 17 2 3"<<endl;
cout<<"1000000000111101 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001000011 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000001001001 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000001001111 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001010101 3 7 13 3 5 17 3 53 7"<<endl;
cout<<"1000000001010111 5 2 3 2 37 2 5 2 3"<<endl;
cout<<"1000000001011001 11 5 281 101 5 67 5 13 19"<<endl;
cout<<"1000000001011011 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001011101 17 2 3 2 1297 2 11 2 3"<<endl;
cout<<"1000000001011111 59 113 7 157 19 1399 7 43 107"<<endl;
cout<<"1000000001100001 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000001100011 23 19 11 105491 5 47 11117 1787 127"<<endl;
cout<<"1000000001100111 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001101011 5 2 3 2 37 2 5 2 3"<<endl;
cout<<"1000000001101101 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001110011 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001110101 5 2 3 2 37 2 5 2 3"<<endl;
cout<<"1000000001111001 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000001111011 31 557 7 19 23 1129 7 5441 241"<<endl;
cout<<"1000000001111101 7 19 43 17 55987 23 7 7 31"<<endl;
cout<<"1000000001111111 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000010000011 167 2 11 2 58427 2 23 2 839"<<endl;
cout<<"1000000010000101 3 2 5 2 7 2 3 2 11"<<endl;
cout<<"1000000010001001 5 2 7 2 1933 2 29 2 157"<<endl;
cout<<"1000000010010001 3 2 5 2 7 2 3 2 7"<<endl;
cout<<"1000000010010111 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000010011001 7 1667 179 13 5 11 23 7 311"<<endl;
cout<<"1000000010011011 11 2 3 2 13 2 47 2 3"<<endl;
cout<<"1000000010011101 3 2 3 2 7 2 3 2 3"<<endl;
cout<<"1000000010100011 3 1259 421 3 5 8893 3 67 17"<<endl;
cout<<"1000000010100111 5 2 3 2 37 2 5 2 3"<<endl;
cout<<"1000000010101001 3 5 13 3 5 43 3 73 7"<<endl;
cout<<"1000000010110011 47 2 3 2 11 2 204311 2 3"<<endl;
cout<<"1000000010110101 3 2 3 2 7 2 3 2 3"<<endl;
  }
}
