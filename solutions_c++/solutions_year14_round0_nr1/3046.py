#include<vector>
#include<iostream>
#include<stdio.h>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<climits>
#include<sstream>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>
 
#define FL(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define SORTF(x) sort(x.begin(),x.end(),func);
#define SORT(x) sort(x.begin(),x.end())
#define pb(x) push_back(x)
#define ll long long
#define SET(v, val) memset(v, val, sizeof(v)) ;
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define ALL(v) v.begin(),v.end()
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }
#define fill(x,n) memset(x,n,sizeof(x))
#define si(x) scanf("%d",&x)
#define si2(x,y) scanf("%d %d",&x,&y)
#define si3(x,y,z) scanf("%d %d %d",&x,&y,&z)
 
#define ss(x) scanf("%s",x)
 
#define sc(x) scanf("%c",&x)
 
#define sf(x) scanf("%f",&x)
 
#define sl(x) scanf("%lld",&x)
#define sl2(x,y) scanf("%lld %lld",&x,&y)
#define sl3(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
 
#define ll long long
#define str string
#define lli long long int
#define ch char
#define fl float
  
#define printi(x) printf("%lld\n",x)
#define printi2(x,y) printf("%lld %lld\n",x,y)
#define printi3(x,y,z) printf("%lld %lld %lld\n",x,y,z)
#define prints(x) printf("%s\n",x)

//#define size(A) ((int)A.size())
#define len(A) ((int)A.length())
#define mp(A,B) make_pair(A,B)

using namespace std;

int main()
{
  int n;
  scanf("%d",&n);
  for(int t=1;t<=n;t++) {
    int r1;
    scanf("%d",&r1);
    vector<int> hash(20,0);
    int val;
    for(int i=1;i<=4;i++) {
	for(int j=1;j<=4;j++) { 
	  scanf("%d",&val);
	  if(i==r1) hash[val]=1;
	}
    }
    int r2;
    scanf("%d",&r2);
    int ans=0;
    int sum=0;
    for(int i=1;i<=4;i++) {
	for(int j=1;j<=4;j++) { 
	  scanf("%d",&val);
	  if(i==r2) {
	    if(hash[val]==1) {
	      ans=val;
	      sum++;
	    }	 
	  }
      }
    }
    printf("Case #%d: ",t); 
    if(sum==0) {
      printf("Volunteer cheated!\n");
    }
    else if(sum==1) {
      printf("%d\n",ans);
    }
    else {
      printf("Bad magician!\n");
    }
  }
  return 0;
} 