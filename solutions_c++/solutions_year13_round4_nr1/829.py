#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <assert.h>
#include <list>
#include <queue>
#include <set>
using namespace std;
static const long long MODNUM = 1000002013;
static const int SIZE = 1e7;
enum Type {
  START,
  END
};
long long int nSum(long long int n) {
  return ((n*(n+1))/2)%MODNUM;
}
long long int abCost(long long int a, long long b, long long n) {
  return (n*(b-a) - nSum(b-a-1))%MODNUM;
}
struct Point {
  int idx;
  mutable long long int count;
  Type type;
  Point(): idx(0), count(0), type(START) {}
  Point(int idx, int count, Type type): idx(idx), count(count), type(type) {}
  bool operator<(const Point &p) const {
    return idx < p.idx ? true : idx > p.idx ? false: type < p.type;
  }
};
int main(int argc, char const *argv[])
{
  int t=0;
  scanf("%d\n", &t);
  for (int iter = 0; iter < t; ++iter)
  {
    int n, m;
    scanf("%d %d\n", &n, &m);
    std::vector<Point> pts;
    long long sum = 0;
    for (int i = 0; i < m; ++i)
    {
      int s,e,p;
      scanf("%d %d %d\n", &s, &e, &p);
      pts.push_back(Point(s, p, START));
      pts.push_back(Point(e, p, END));
      sum += (abCost(s, e, n)*p)%MODNUM;
    }
    long long newSum = 0;
    sort(pts.begin(),pts.end());
    set<Point> pts2;
    // std::set<Point> pts2(pts.begin(), pts.end());
    for (int i = 0; i < pts.size(); ++i)
    {
      if(pts2.find(pts[i]) != pts2.end()) {
        pts2.find(pts[i])->count += pts[i].count;
      }
      else
        pts2.insert(pts[i]);
    }
    // printf("enteringh for the first time..\n");
    while(pts2.size()) {
      set<Point>::iterator start = (pts2.begin());
      int curMin = 999999999;
      set<Point>::iterator minStart = pts2.begin(), minEnd = pts2.end();
      assert(minStart->type == START);
      for(set<Point>::iterator it = pts2.begin(); it != pts2.end(); it++) {
        if(it->type == START) {
          start = it;
          continue;
        }
        if(it->idx - start->idx < curMin) {
          curMin = it->idx - start->idx;
          minStart = start;
          minEnd = it;
        }
      }
      assert(minEnd != pts2.end());
      assert(minStart != minEnd);
      Point ms = *minStart, me = *minEnd;
      pts2.erase(minStart); pts2.erase(minEnd);
      // printf("%d %d %d removed!\n", ms.idx, me.idx, min(ms.count, me.count));
      if(ms.count > me.count)
        pts2.insert(Point(ms.idx, ms.count - me.count, START));
      else if(ms.count < me.count)
        pts2.insert(Point(me.idx, me.count - ms.count, END));
      newSum += (abCost(ms.idx, me.idx, n)*(long long)min(ms.count, me.count)) % MODNUM;
    }
    sum %= MODNUM;
    newSum %= MODNUM;
    printf("Case #%d: %lld\n", iter+1, ((sum-newSum)%MODNUM+MODNUM)%MODNUM);
  }
  return 0;
}