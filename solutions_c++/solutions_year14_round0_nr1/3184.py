#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<map>
#include<list>
#include<string.h>
#include<sstream>
#include<set>
#include<ctype.h>
#include<queue>
#include<ctime>
using namespace std;

#define SWAP(a, b) ((&(a) == &(b)) || (((a) -= (b)), ((b) += (a)), ((a) = (b) - (a))))

#define ll long long int
#define ull unsigned long long 64
#define FOR(i,n) for(i=0;i<n;i++)
#define REP(i,n) for(i=n-1;i>=0;i--)
#define init(arr) memset(arr,0, sizeof(arr))

#define vi vector<int>
#define vii vector< vi >
#define ALL(ch) ch.begin(),ch.end()
#define pi pair<int,int>
#define PB push_back

#define sc(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)

#define MAX 1000
#define MAXE 500000

/******
 * 
ostringstream oss;
oss <<1<<"any string";
string str= oss.str();
*
*****/

// Fast IO 

// assert(condition to check); if the condition fails, it will cause the abnormal termination of the program. 

// #undef NDEBUG  // TO disable all asertions from the source code, if used.

const int size = 1<<18;
char buff[size];
int lp=0,up=0;
char read_char()
{
  if(lp==up)
  {
    up=fread(buff,sizeof(char),size,stdin);
    if(up==0)
      return 0;
    lp=0;
  }
  return buff[lp++];
}
int read_int()
{
  char c;
  do{
    c=read_char();
  }while(c<'0' || c>'9');
  
  int val=0;
  for(;c>='0' && c<='9';c=read_char())
    val=(val<<3) +(val<<1) + c-'0';
  
  return val;
}


main()
{
  int t,i,j,n,m,x=0, count, num=0;
  sc(t);
  while(t--)
  {
  	count=0;
  	sc(n);
  	int ch[4][4];
  	FOR(i,4) FOR(j,4) sc(ch[i][j]);

  	int arr[4][4];
  	sc(m);
  	FOR(i,4) FOR(j,4) sc(arr[i][j]);

  	num = 0;
  	FOR(i,4) FOR(j,4) if(ch[n-1][i] == arr[m-1][j]){ num = ch[n-1][i]; count++;}

  	printf("Case #%d: ", ++x);
  	if(count==0) puts("Volunteer cheated!");
  	else if(count==1) printf("%d\n", num);
  	else puts("Bad magician!");
  }
  return 0;
}
