#include <cstdio>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <utility>
#include <cinttypes>

typedef std::vector<std::vector<int>> grid_t;

bool hfill( grid_t& into, int x, const std::vector<int> from )
{
  for (int i=0;i<from.size();++i)
  {
    if (into[x][i]==0)
      into[x][i]=from[i];
    else if (into[x][i]!=from[i])
      return false;
  }
  return true;
}

bool vfill( grid_t& into, int y, const std::vector<int> from )
{
  for (int i=0;i<from.size();++i)
  {
    if (into[i][y]==0)
      into[i][y]=from[i];
    else if (into[i][y]!=from[i])
      return false;
  }
  return true;
}

bool is_solved = false;

void solve( const std::vector< std::vector<int> >& h,
            int hpos,
            int line,
            const grid_t& grid,
            int n,
            int x,
            int y
  )
{
  if (is_solved) return;
  if ( x == line ) ++x;
  if (hpos==h.size())
  {
    is_solved=true;
    for (int i=0;i<n;++i)
      printf(" %d",grid[line][i]);
    return;
  }

  const std::vector<int>& next = h[hpos];

  if ( x < n )
  {
    grid_t g = grid;
    bool b = hfill( g, x, next );
    if ( b )
      solve( h, hpos+1, line, g, n, x+1, y );
  }
  if ( y < n )
  {
    grid_t g = grid;
    bool b = vfill( g, y, next );
    if ( b )
      solve( h, hpos+1, line, g, n, x, y+1 );
  }
}

void do_solve( const std::vector< std::vector<int> >& h, int n )
{
  is_solved = false;
  for ( int i =0 ;i < n; ++i )
  {
    if ( is_solved ) break;
    grid_t g(n);
    for ( auto& gi : g )
      gi.resize(n);
    solve(h,0,i,g,n,0,0);
  }
}

int main(int arng, char**argv)
{
  int ncase;
  scanf("%d",&ncase);
  for (int icase=0;icase<ncase;++icase)
  {
    std::vector< std::vector<int> > h;
    int n;
    scanf("%d",&n);
    for ( int i = 0; i < 2*n-1; ++i )
    {
      h.emplace_back();
      h.back().resize(n);
      for ( int k=0;k<n;++k)
      {
        scanf("%d",&h[i][k]);
      }
    }
    printf("Case #%d:",icase+1 );
    // sort it
    std::sort( h.begin(), h.end(), [](const std::vector<int>& l, const std::vector<int>& r)->bool
               {
                 for ( int i=0;i<l.size(); ++i)
                 {
                   if (l[i]<r[i])
                     return true;
                   if (r[i]<l[i])
                     return false;
                 }
                 return false;
               }
      );
    do_solve(h,n);
    printf("\n");
  }
  return 0;
}
