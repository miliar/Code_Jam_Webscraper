#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <set>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

typedef long long LL;

template<typename T, size_t n_max, bool debug = 0>
struct Binom
{
	Binom()
	{
		for(size_t i=0; i<n_max; ++i){ A[0][i] = 0; A[i][0] = 1; }
		for(size_t n=1; n<n_max; ++n) for(size_t k=1; k<n_max; ++k)
			A[n][k] = A[n-1][k-1]+A[n-1][k];
	}

	template<typename Mod> Binom(Mod m)
	{
		for(size_t i=0; i<n_max; ++i){ A[0][i] = 0%m; A[i][0] = 1%m; }
		for(size_t n=1; n<n_max; ++n) for(size_t k=1; k<n_max; ++k)
			A[n][k] = (Mod(A[n-1][k-1])+Mod(A[n-1][k]))%m;
	}

	T operator()(size_t n, size_t k) const
	{
		if(debug) assert(n<n_max && k<n_max);
		return A[n][k];
	}

	T A[n_max][n_max];
};

enum { M = 1000000007, L = 'Z'-'A'+1 };
Binom<int,1100> Bn(M);

int main()
{
  int t; std::cin >> t;
  FOR(_,1,t)
  {
    std::multiset<std::string> S;
    std::set<std::string> S2;
    int m,n; std::cin >> m >> n;
    REP(i,m)
    {
      std::string s; std::cin >> s;
      FOR(i,0,s.size()) S.insert(s.substr(0,i));
    }
    //for(auto s : S) printf("%s\n",s.c_str()); 
    LL res = 0, times = 1;
    for(const std::string &s : S)
    {
      if(S2.count(s)) continue; S2.insert(s);
      int a = S.count(s), e = a; //printf("a = %d\n",a); 
      int A[30]; REP(c,L){ A[c] = S.count(s+char(c+'A')); e -= A[c]; }
      res += a = std::min(a,n);
      LL t1 = 0;
      FOR(aa,0,a)
      {
        LL t2 = Bn(a,aa); if(aa&1) t2 = (M-t2)%M;
        REP(c,L) t2 = t2*Bn(a-aa,std::min(a,A[c]))%M;
        t2 = t2*Bn(a-aa,e)%M;
        t1 = (t1+t2)%M;
      }
      times = times*t1%M;
      //printf("%s = %d; e = %d\n",s.c_str(),t1,e);
    }
    printf("Case #%d: %lld %lld\n",_,res,times);
  }
  return 0;
}
