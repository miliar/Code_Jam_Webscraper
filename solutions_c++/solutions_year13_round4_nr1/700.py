#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

using namespace std;

struct pairs
{
  pairs(long long s, long long e, long long p_)
    :st(s), ed(e), p(p_) {}
  long long st, ed, p;
};

struct point
{
  point(long long n_)
    :n(n_), left(0), out(0) {}
  long long n, left, out;
};

long long getCost(long long st, long long ed, long long p, long long N)
{
  if(ed <= st)
    {return 0;}
  long long d = ed - st;
  long long cost = d*(2*N-d+1)/2;
  cost %= 1000002013;
  cost *= p;
    //cout << st << " " << ed << " " << p << " " << cost << endl;
  return cost%1000002013;
}

int main()
{
  int cnt;
  cin >> cnt;
  for(int i = 0; i < cnt; ++i)
    {
      cerr << i << endl;
      int N, M;
      cin >> N >> M;
      vector<pairs> ps;
      set<long long> valid;
      long long totCost = 0;
      for(int j = 0; j < M; ++j)
	{
	  long long s,e,c;
	  cin >> s >> e >> c;
	  if(e>s)
	    {
	      long long dd = e -s;
	      long long th = dd*(2*N-dd+1)/2;
	      th %= 1000002013;
	      th *= c;
	      th %= 1000002013;
	      totCost += th;
	      totCost %= 1000002013;
	    }
	  ps.push_back(pairs(s,e,c));	  
	  valid.insert(s);
	  valid.insert(e);
	}
      vector<point> stations;
      map<long long, long long> convert;
      long long cnt = 0;
      for(set<long long>::iterator iter = valid.begin(); iter != valid.end(); ++iter)
	{
	  stations.push_back(point(*iter));
	  convert[*iter] = cnt++;
	}
      for(int j = 0; j < ps.size(); ++j)
	{
	  long long st = convert[ps[j].st];
	  long long ed = convert[ps[j].ed];
	  stations[st].left += ps[j].p;
	  stations[ed].out += ps[j].p;
	}
      long long cost2 = 0;
      for(int j = 0; j < stations.size(); ++j)
	{
	  long long out = stations[j].out;
	  for(int k = j; out > 0 && k >= 0; --k)
	    {
	      if(stations[k].left >= out)
		{
		  stations[k].left -= out;
		  cost2 += getCost(stations[k].n, stations[j].n, out, N);
		  out = 0;
		}
	      else
		{
		  cost2 += getCost(stations[k].n,stations[j].n,stations[k].left, N);
		  out -= stations[k].left;
		  stations[k].left = 0;
		}
	      cost2 %= 1000002013;
	    }
	}
      //cout << cost2 << endl;
      long long diff = (totCost-cost2+1000002013)%1000002013;
      
      cout << "Case #" << i+1 << ": " << diff << endl;;
    }
}
