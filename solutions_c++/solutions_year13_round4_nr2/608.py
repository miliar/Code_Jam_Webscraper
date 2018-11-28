using namespace std;
#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll; 
typedef pair<int,int> pii; 
#define FOR(i,n) for (int i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define MP make_pair
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d\n",x)
#define split(str) {vs.clear();istringstream ss(str);while(ss>>(str))vs.push_back(str);}
#define PI 3.141592653589793
int main()
{
  int t;
  sf(t);
  int temp = 1;
  while(t--)
  {
    ll n,p;
    cin>>n>>p;
    vector<bool> precord(n,true);
    int i = 0;
    ll mid = 1;
    ll teams = 1;
    FOR(i,n-1)
    {
      mid *= 2;
    }
    teams = mid*2;
    int firstW = 55; // zero based
    int firstL = 55; // zero based
    while(i < n)
    {
      if(p <= mid) 
      {
	precord[i] = false;
	if(firstW == 55)
	  firstW = i;
      }
      else
      {
	p -= mid;
	if(firstL == 55)
	  firstL = i;
      }
      mid /= 2;      
      i++;
    }
    int worst = 1;
    for(;worst<teams;worst++)
    {
      vector<bool> lovrec(n,false);
      int locW = 0;
      int left = worst;
      while(true)
      {
	if(left == 0)break;
	lovrec[locW] = true;
	locW ++;
	left--;
	left /= 2;
      }
      if(lovrec > precord)break;
    }
    
    int best = teams - 1;
    for(;best>=0;best--)
    {
      vector<bool> lovrec(n,true);
      int locL = 0;
      int left = teams - best -1;
      while(true)
      {
	if(left == 0)break;
	lovrec[locL] = false;
	locL ++;
	left--;
	left /= 2;
      }
      if(lovrec <= precord)break;
    }
    //FOR(i,n)
      //cout<<precord[i]<<endl;
    printf("Case #%d: %d %d\n",temp,worst - 1, best);
    temp++;
  }
}