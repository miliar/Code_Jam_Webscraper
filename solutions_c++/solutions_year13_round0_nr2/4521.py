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
#include <cstring>
#include <string>
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
  int temp = t;
  while(t--)
  {
    cout<<"Case #"<<temp - t<<": ";
    int n,m;
    sf(n);sf(m);
    int arr[n][m];
    bool val[n][m];
    
    memset(val, false, sizeof(val));
    
    FOR(i,n)
    {
      FOR(j,m)
      {
	int a;
	cin>>a;
	arr[i][j] = a;
      }
    }
    
    FOR(i,n)
    {
      int maxval = -1;
      FOR(j,m)
	maxval = max(maxval,arr[i][j]);
      
      FOR(j,m)
	if(maxval == arr[i][j])
	  val[i][j]=true;
    }
    
    FOR(j,m)
    {
      int maxval = -1;
      FOR(i,n)
	maxval = max(maxval,arr[i][j]);
      
      FOR(i,n)
	if(maxval == arr[i][j])
	  val[i][j]=true;
    }
    
    bool yes = true;
    
    FOR(i,n)
      FOR(j,m)
	if(!val[i][j])
	  yes = false;
    if(yes)
      cout<<"YES"<<endl;
    else
      cout<<"NO"<<endl;
  }
}