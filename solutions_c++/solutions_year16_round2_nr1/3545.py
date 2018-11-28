#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class An
{
public:
  An(std::string const &s);
  bool subset(An const &x) const;
  bool empty() const;
  bool less(An const &x) const;
  An &operator-=(An const &x);
  An &operator+=(An const &x);

private:
  enum { SIZE = 'Z' - 'A' + 1 };
  int cnt[SIZE];
};


bool An::empty() const
{
  for ( int i=0; i<SIZE; ++i )
    if ( cnt[i] != 0 )
      return false;
  return true;
}


bool An::less(An const &x) const
{
  int i = 0;
  while ( i < SIZE and cnt[i] == x.cnt[i] )
    ++i;
  return i < SIZE and cnt[i] < x.cnt[i];
}


inline bool operator<(An const &a1, An const &a2)
{
  return a1.less(a2);
}


bool An::subset(An const &x) const
{
  for ( int i=0; i<SIZE; ++i )
    if ( cnt[i] > x.cnt[i] )
      return false;
  return true;
}


An::An(std::string const &s)
{
  for ( int i=0; i<SIZE; ++i )
    cnt[i] = 0;
  for ( size_t i=0; i<s.length(); ++i )
  {
    int c = toupper(s[i]) - 'A';
    if ( c >= 0 and c < SIZE )
      ++cnt[c];
  }
}

An &An::operator-=(An const &x)
{
  for ( int i=0; i<SIZE; ++i )
    cnt[i] = std::max(cnt[i] - x.cnt[i], 0);
  return *this;
}


An &An::operator+=(An const &x)
{
  for ( int i=0; i<SIZE; ++i )
    cnt[i] += x.cnt[i];
  return *this;
}

using WordList = std::vector<std::pair<An, int>>;

WordList create_dict(An const &orig)
{
  WordList r;
  int d = 0;
  for ( std::string w: {"ZERO", "ONE", "TWO", "THREE", "FOUR",
      "FIVE", "SIX", "SEVEN", "EIGHT",
      "NINE"} )
  {
    An na(w);
    if ( !na.subset(orig) )
    {
      ++d;
      continue;
    }
    r.push_back(std::make_pair(na, d));
    ++d;
  }
  return r;
}

WordList D;
An *current;
std::vector<size_t> idx;

bool back_track()
{
  if ( current->empty() )
    return true;
  for ( size_t i = 0; i != D.size(); ++i )
    if ( D[i].first.subset(*current) )
    {
      *current -= D[i].first;
      idx.push_back(i);
      if ( back_track() )
        return true;
      idx.pop_back();
      *current += D[i].first;
    }
  return false;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    std::string S;
    std::cin >> S;
    An c(S);
    current = &c;
    D = create_dict(c);
    idx.clear();
    if ( back_track() )
    {
      std::vector<int> sol;
      for ( size_t i: idx )
        sol.push_back(D[i].second);
      std::sort(sol.begin(), sol.end());
      std::cout << "Case #" << t << ": ";
      for ( int x: sol )
        std::cout << x;
      std::cout << '\n';
    }
  }
  return 0;
}
