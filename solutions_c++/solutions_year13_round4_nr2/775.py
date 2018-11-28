#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;

int n,p;
int m;
pair<int,int> todos[5000];
void calc(int a, int b, int kk){
  if(todos[b].second == kk)swap(a,b);
  assert(todos[a].first==todos[b].first);
  if(todos[a].second == kk){
    if(todos[b].second==-1){
      todos[b].first=2*todos[b].first;
      todos[a].first=2*todos[a].first+1;
    }else{
      todos[b].first=2*todos[b].first+1;
      todos[a].first=2*todos[a].first;
    }
  }
  else {
      if(todos[a].second<todos[b].second){
	todos[a].first=2*todos[a].first;
	todos[b].first=2*todos[b].first+1;
      }
      else{
	todos[a].first=2*todos[a].first+1;
	todos[b].first=2*todos[b].first;
      }
      
  }

}
int best(int a){
  for(int i=0;i<a;i++)todos[i]=make_pair(0,-1);
  for(int i=a;i<m;i++)todos[i]=make_pair(0,1);
  todos[m-1]=make_pair(0,2); 
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j+=2){
      calc(j,j+1,2);
    }
    stable_sort(todos, todos+m);
  }
  for(int i=0;i<m;i++)
    assert(todos[i].first==i);
  for(int i=0;i<m;i++)
    if(todos[i].second==2)return i;
}

int worst(int a){
  todos[0]=make_pair(0,-2); 
  for(int i=1;i<=a;i++)todos[i]=make_pair(0,-1);
  for(int i=a+1;i<m;i++)todos[i]=make_pair(0,1);
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j+=2){
      calc(j,j+1,-2);
    }
    stable_sort(todos, todos+m);
  }
  for(int i=0;i<m;i++)
    assert(todos[i].first==i);
  for(int i=0;i<m;i++)
    if(todos[i].second==-2)return i;
}

int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d %d",&n,&p);
      m = (1<<n);
      int r1 = m, r2 = -1;
      for(int i=0;i<m;i++){
	int b = best(i);
	int c = worst(i);
	if(b<p)r2 = max(r2,i);
	if(c>=p)r1 = min(r1,i);
      }
      printf("Case #%d: %d %d\n",pp,r1-1,r2);
    }
  return 0;
}
