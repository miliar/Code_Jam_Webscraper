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

void printvec(std::vector<int> v,int len)
{
  printf("\nvec:");
  for (int i=0;i<len;++i)
    printf(" %d",v[i]);
  printf("\n");
}

int solve( std::vector<int> bff )
{
  int maxres = 0;
  int n = bff.size();
  std::vector<int> perms(n);
  for (int i=0;i<n;++i)
    perms[i]=i;
  do {
    for (int i=0;i<n;++i)
    {
      bool ok = true;
      for (int k=0;k<=i;++k)
      {
        int probe = perms[k];
        int right = perms[ (k+1)%(i+1) ];
        int left = perms[ (k+i+1-1)%(i+1) ];
        if ( bff[probe] != right && bff[probe] != left )
        {
          ok = false;
          break;
        }
      }
      if (ok)
      {
        maxres = std::max(maxres,i+1);
//        if ( i+1 == 8 )
//          printvec(perms,8);
//        printvec(b
      }
    }
//    std::cout << myints[0] << ' ' << myints[1] << ' ' << myints[2] << '\n';
  } while ( std::next_permutation(perms.begin(),perms.end() ) );
  return maxres;
}

int main(int arng, char**argv)
{
  int ncase;
  scanf("%d",&ncase);
  for (int icase=0;icase<ncase;++icase)
  {
    int n;
    scanf("%d",&n);
    std::vector<int> bff(n);
    for ( int i=0; i<n;++i)
    {
      scanf("%d",&bff[i]);
      --bff[i];
    }
    printf("Case #%d: %d\n",icase+1,solve(bff));
  }
  return 0;
}
