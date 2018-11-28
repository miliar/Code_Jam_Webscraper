#include<vector>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<iomanip>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define INF (int)1e9
#define LINF (long long)1e18
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?(-(x)):(x))
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define foreach(v,c) for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)

int main()
{
  int tc; s(tc);
  int tests = tc;
  while(tc--) {
    // Inputs
    vector<int> numbers;
    int ans1; s(ans1);
    REP(i, 16) {
      int inp; s(inp);
      if(i>=((ans1-1)*4) && i<(((ans1-1)*4)+4))
        numbers.push_back(inp);
    }
    int ans2; s(ans2);
    REP(i, 16) {
      int inp; s(inp);
      if(i>=((ans2-1)*4) && i<(((ans2-1)*4)+4))
        numbers.push_back(inp); 
    }
    // Idea
    set<int> uniq(numbers.begin(), numbers.end());
    // Answer
    if(uniq.size() == 7) {
      int sum = 0;
      REP(i, 8)
      {
        sum += numbers[i];
      }
      for(set<int>::iterator it=uniq.begin();it!=uniq.end();it++)
      {
        sum -= (*it);
      }
      cout<<"Case #"<<(tests-tc)<<": "<<sum<<endl;
    }
    else if(uniq.size() == 8)
      cout<<"Case #"<<(tests-tc)<<": "<<"Volunteer cheated!"<<endl;
    else
      cout<<"Case #"<<(tests-tc)<<": "<<"Bad magician!"<<endl; 
  }
  return 0;
}

