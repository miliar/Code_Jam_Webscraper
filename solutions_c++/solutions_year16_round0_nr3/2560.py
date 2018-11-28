#include <iostream>
#include <vector>
#include <random>
#include <set>
#include <cstdint>


template<typename T>
T sqr(T x)
{
  return x*x;
}



std::vector<unsigned> dijkstra_primes(unsigned N)
{
  std::vector<unsigned> P;
  P.reserve(N);
  P.push_back(2);
  std::vector<unsigned> Q;
  auto is_prime = [&Q, &P](unsigned x){
    for ( unsigned k = 1; k < Q.size(); ++k )
    {
      if ( x > Q[k] )
        Q[k] += P[k];
      if ( x == Q[k] )
        return false;
    }
    return true;
  };
  unsigned x = 1, limit = 4;
  while ( P.back() < N )
  {
    do
    {
      x += 2;
      if ( x >= limit )
      {
        Q.push_back(limit);
        limit = sqr(P[Q.size()]);
      }
    } while ( !is_prime(x) );
    P.push_back(x);
  }
  return P;
}


using digits = std::vector<unsigned>;


bool is_equal(digits const &D, unsigned b, unsigned p)
{
  std::uint64_t s = 0;
  for ( auto d: D )
  {
    s = s*b + d;
    if ( s > std::numeric_limits<unsigned>::max() )
      return false;
  }
  return s == p;
}



unsigned proof(digits const &D, unsigned b,
    std::vector<unsigned> const &plist)
{
  for ( unsigned p: plist )
  {
    unsigned s = 0;
    for ( auto d: D )
      s = (s*b + d)%p;
    if ( s == 0 )
      return is_equal(D, b, p) ? -1 : p;
  }
  return -1;
}


unsigned to_num(digits const &D, unsigned base)
{
  unsigned r = 0;
  for ( unsigned d: D )
    r = r*base + d;
  return r;
}


using proofs = std::vector<unsigned>;
std::vector<std::pair<digits, proofs>> gen_coins(int n, int j)
{
  std::mt19937 rng;
  std::uniform_int_distribution<uint32_t> zo(0, 1);
  std::vector<std::pair<digits, proofs>> r;
  std::set<unsigned> seen;
  auto P = dijkstra_primes(100000);
  while ( int(r.size()) < j )
  {
    digits D; D.reserve(n);
    D.push_back(1);
    for ( int i = 0; i < n - 2; ++i )
      D.push_back(zo(rng));
    D.push_back(1);
    {
      auto x = to_num(D, 2);
      if ( seen.find(x) != seen.end() )
        continue;
    }
    proofs pp;
    for ( int b = 2; b <= 10; ++b )
    {
      auto p = proof(D, b, P);
      if ( p == unsigned(-1) )
        break;
      pp.push_back(p);
    }
    if ( pp.size() == 9 )
    {
      r.emplace_back(D, pp);
      seen.insert(to_num(D, 2));
    }
  }
  return r;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int N, J;
    std::cin >> N >> J;
    std::cout << "Case #" << t << ":\n";
    for ( auto &p: gen_coins(N, J) )
    {
      for ( auto d: p.first )
        std::cout << d;
      for ( auto d: p.second )
        std::cout << ' ' << d;
      std::cout << '\n';
    }
  }
  return 0;
}
