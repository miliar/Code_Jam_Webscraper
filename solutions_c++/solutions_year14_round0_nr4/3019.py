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
  int i,j,k,m,n,t,x=0;
  double a,b,c;
  int count =0, opt_cnt=0;
  sc(t);
  while(t--){
  	sc(n);
 	vector< double> ch(n), arr(n);

 	vi visited(n,0);
 	FOR(i,n) scanf("%lf", &ch[i]);
 	FOR(i,n) scanf("%lf", &arr[i]);

 	sort(ALL(ch));
 	sort(ALL(arr));

 	count=0;
 	opt_cnt=0;
 	int flag=0;
 	FOR(i,n)
 	{
 		flag = 0;
 		FOR(j,n)
 		{
 			if(arr[j]> ch[i] && !visited[j]) {visited[j] = 1; opt_cnt++; flag = 1; break;}
 		}

 		if(!flag) break;
 	}

 	opt_cnt = n - opt_cnt;

 	FOR(i,n) visited[i] = 0;

 	//FOR(i,n) printf("%lf ", ch[i]);
 //	puts("");
 //	FOR(i,n) printf("%lf ", arr[i]);
 //	puts("");

 	j=0;
 	int temp=0;
 	FOR(i,n)
 	{
 		if(ch[i]> arr[temp]){ temp++; count++;}
 		//for(j=temp;j<n;j++) if(ch[i]<arr[j]) { break; } else {count++; temp = j+1; break;}
 	}

 	printf("Case #%d: %d %d\n", ++x, count, opt_cnt);
  }
  return 0;
}
