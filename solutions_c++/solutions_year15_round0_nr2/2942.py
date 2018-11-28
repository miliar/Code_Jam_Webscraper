#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <cassert>
using namespace std;

int D;
int P[1024];

typedef pair<int,int> Pii;

int solve()
{
  const int mx = *max_element(P, P+D);

  int ans = 1<<28;
  for (int val = 1; val <= mx; val++)
  {
    priority_queue<int> pq;
    for (int i = 0;i<D;i++)
      pq.push(P[i]);

    int sp=0;
    while (!pq.empty())
    {
      int e = pq.top(); pq.pop();
      if (e <= val)
      {
        //printf("val=%d, e=%d, sp=%d\n", val, e, sp);
        ans = min(ans, val + sp);
        break;
      }
      int rest = e - val;
      sp++;
      pq.push(rest);
    }
  }
  return ans;
}

int main()
{
  int T;
  cin>>T;
  for(int z=1;z<=T;z++)
  {
    cin>>D;
    for(int i=0;i<D;i++)
    {
      cin>>P[i];
    }

    //cout<<solve()<<endl;
    printf("Case #%d: %d\n", z, solve());
  }

  return 0;
}
