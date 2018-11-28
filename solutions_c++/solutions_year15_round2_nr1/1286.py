/*
*
* solved by Ahmed Kamal
*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int> 
#define ii pair<int,int> 
#define vii vector< pair<int,int> > 

#define ALL(v)        ((v).begin()), ((v).end())
#define SZ(v)       ((int)((v).size()))
#define CLR(v, d)     memset(v, d, sizeof(v))
#define REP(i, n)   for(int i=0;i<(int)(n);++i)
#define LOOP(i,b, n)    for(int i=(b);i<(int)(n);++i)

#define sc(x) scanf("%d",&x)
#define DSC(x) int x; scanf("%d",&x)
#define DSC2(x,y) int x,y; scanf("%d %d",&x,&y)

#define PB  push_back
#define MP  make_pair
double const EPS = 2.22045e-016;
#define INF (1<<29)


typedef vector<double>    VD;
typedef vector<string>    VS;
void print_v(vi arr){
int n = SZ(arr);
  REP(i,n)
    if(i == n-1)
       printf("%d\n",arr[i] );
     else
      printf("%d ", arr[i]);
}

int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }

bool visit[1100006];

int main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
#endif
DSC(ts);
REP(t,ts){
  CLR(visit, false);
  DSC(n);
  // printf("n = %d\n",n );
  queue<int> qu;
  qu.push(1);
  int ans = 1;
  if(n == 1){
    printf("Case #%d: %d\n",t+1,1);
    continue;
  }

  while(!qu.empty()){
    vi arr;
    while(!qu.empty()){
      int u = qu.front();
      qu.pop();
      if(u == n)
        break;
      string s;
      stringstream ss;
      ss << u;
      ss >> s;
      reverse(ALL(s));
      ss.clear();
      ss<<s;
      int k;
      ss>>k;
      if(!visit[k])
        arr.push_back(k);
      if(!visit[u+1])
        arr.push_back(u+1);
      // printf("%d %d\n",k,u+1 );
      visit[u+1] = 1;
      visit[k] = 1;
    }
    ans++;
    bool  g = false;
    REP(i,SZ(arr)){
      if(arr[i] == n)
        g = true;
      qu.push(arr[i]);
    }
    // print_v(arr );
    // printf("one\n");
    if(g)
      break;
  }  
  printf("Case #%d: %d\n",t+1,ans );
}
return 0; 
}
