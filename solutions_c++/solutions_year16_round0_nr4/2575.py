#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<math.h>
//structures
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<list>
#include<deque>
#include<string>
#include<complex>
#include<sstream>
#include<cctype>
#include<iomanip>
#include<bitset>

using namespace std;

#define REP(i,n)	for(int i=1;i<=n;i++)
#define FOR(i,n)	for(int i=0;i<n;i++)
#define FOB(i,n)	for(int i=n;i>=1;i--)
#define druha(x) ((x)*(x))
#define MP(x,y)	make_pair((x),(y))
#define infinity 2000000999
#define ii pair<int, int>
#define lli long long int
#define lili pair<lli, lli>
#ifdef EBUG
#define DBG	if(1)
#else
#define DBG	if(0)
#endif

int getn()
{
  int h;
  scanf("%d",&h);
  return h;
}

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>&par) {
  cout<<par.first<<" "<<par.second<<endl;
  return out;
}

template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  FOR(i, v.size()){
    if(i) cout<<" ";
    cout<<v[i];
  }
  cout<<endl;
  return out;
}

int main(){
  int t = getn();
  FOR(l, t){
    int k = getn();
    int c = getn();
    int s = getn();
    cout << "Case #" << l + 1 << ": ";
    FOR(i, s) cout << (i ? " " : "") << i + 1;
    cout << endl;
  }
}
