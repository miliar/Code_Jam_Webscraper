#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int, int> pii;

void solve()
{
  int N;
  vector<pii> ans;
  priority_queue<pii> heap;

  scanf("%d", &N);
  for(int i=0; i<N; i++)
  {
    int t;
    scanf("%d", &t);
    heap.emplace(make_pair(t, i));
  } 
  
  //pair 의 first -> 인원수, second -> 정당
  while(!heap.empty())
  {
    pii candi(-1, -1);
    for(int i=0; i<2; i++)
    {
      if (heap.empty()) break;
      pii top = heap.top(); heap.pop();
      if(i==0)
        candi.first = top.second;
      else 
        candi.second = top.second;
      top.first = top.first - 1;
      if(top.first > 0)
        heap.emplace(top);
    }
    ans.push_back(candi);
  }

  if (ans.size() > 1 && ans.back().second == -1)
  {
    pii t = ans.back();
    ans.pop_back();
    pii t2 = ans.back();
    ans.pop_back();
    vector<int> tmp;
    tmp.push_back(t2.first);
    tmp.push_back(t2.second);
    tmp.push_back(t.first);
    sort(tmp.begin(), tmp.end());
    ans.push_back(make_pair(tmp[0], -1));
    ans.push_back(make_pair(tmp[2], tmp[1]));
  }
  
  //print answer
  for(int i=0; i<ans.size(); i++)
  {
    if (ans[i].second == -1)
      printf("%c", ans[i].first+'A');
    else
      printf("%c%c", ans[i].first+'A', ans[i].second+'A');
    printf("%c",i==ans.size()-1 ? '\n' : ' ');
  }
}

int main(){
  freopen("large.in", "r", stdin);
  freopen("large.out", "w", stdout);
  int tc;
  scanf("%d", &tc);
  for(int i=1; i<=tc; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }
}
