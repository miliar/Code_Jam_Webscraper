#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>


using Board = std::vector<std::vector<int>>;


Board b, order;
bool visited[21][1<<20];
std::vector<char> rows, cols;

bool match(int k, unsigned used)
{
  if ( k >= int(order.size()) )
    return true;
  if ( visited[k][used] )
    return false;
  auto &v = order[k];
  int N = b.size();
  for ( int r = 0; r < N; ++r )
  {
    if ( rows[r] )
      continue;
    bool good = true;
    for ( int c = 0; c < N; ++c )
      if ( b[r][c] != 0 && b[r][c] != v[c] )
      {
        good = false;
        break;
      }
    if ( good )
    {
      std::vector<int> m(N);
      for ( int c = 0; c < N; ++c )
      {
        m[c] = b[r][c];
        b[r][c] = v[c];
      }
      rows[r] = true;
      if ( match(k + 1, used) )
        return true;
      rows[r] = false;
      for ( int c = 0; c < N; ++c )
        b[r][c] = m[c];
    }
  }
  for ( int c = 0; c < N; ++c )
  {
    if ( cols[c] )
      continue;
    bool good = true;
    for ( int r = 0; r < N; ++r )
      if ( b[r][c] != 0 && b[r][c] != v[r] )
      {
        good = false;
        break;
      }
    if ( good )
    {
      std::vector<int> m(N);
      for ( int r = 0; r < N; ++r )
      {
        m[r] = b[r][c];
        b[r][c] = v[r];
      }
      cols[c] = true;
      if ( match(k + 1, used|(1<<k)) )
        return true;
      cols[c] = false;
      for ( int r = 0; r < N; ++r )
        b[r][c] = m[r];
    }
  }
  visited[k][used] = true;
  return false;
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    int N;
    std::cin >> N;
    order.clear();
    order.resize(2*N - 1);
    for ( int i = 0; i < 2*N - 1; ++i )
    {
      order[i].resize(N);
      for ( int j = 0; j < N; ++j )
        std::cin >> order[i][j];
    }
    std::sort(order.begin(), order.end());
    b.clear();
    b.resize(N);
    for ( int i = 0; i < N; ++i )
      b[i].resize(N);
    rows.clear(); rows.resize(N);
    cols.clear(); cols.resize(N);
    std::memset(visited, 0, sizeof(visited));
    match(0, 0);
    for ( int i = 0; i < N; ++i )
    {
      if ( !rows[i] )
      {
        std::cout << "Case #" << t << ':';
        for ( int c = 0; c < N; ++c )
          std::cout << ' ' << b[i][c];
        std::cout << '\n';
        break;
      }
      if ( !cols[i] )
      {
        std::cout << "Case #" << t << ':';
        for ( int r = 0; r < N; ++r )
          std::cout << ' ' << b[r][i];
        std::cout << '\n';
        break;
      }
    }
  }
  return 0;
}
