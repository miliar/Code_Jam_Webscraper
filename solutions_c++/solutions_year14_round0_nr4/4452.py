# /*
this_md5="$(md5sum < "$0" | cut -d' ' -f1)"
last_md5="$(readelf -p SOURCE_FILE_HASH "${0%.cpp}" 2>/dev/null | awk '/\[ *0\]/ { print $3 }')"
if [ "$this_md5" != "$last_md5" ]; then
g++ -pipe -Wall -Wextra -std=c++11 -g -march=native -Og -DTHIS_MD5="\"$this_md5\"" -o "${0%.cpp}" "$0" ||
exit 1
fi
exec "${0%.cpp}" "$@"
exit 1
# */
#ifndef THIS_MD5
# define THIS_MD5 "not set"
#endif
char MD5[] __attribute__((section ("SOURCE_FILE_HASH"))) = THIS_MD5;

#include <cstdlib>
#include <iostream>
#include <set>
#include <tuple>
#include <cassert>

using namespace std;

namespace
{
  double ken_choose( double told_naomi, set< double > *ken )
  {
    auto it = ken->lower_bound( told_naomi );
    double res;
    if( it != ken->end() )
      {
        res = *it;
        ken->erase( it );
      }
    else
      {
        res = *ken->begin();
        ken->erase( ken->begin() );
      }
    return res;
  }

  double naomi_choose_war( set< double > *naomi )
  {
    double res = *naomi->rbegin();
    naomi->erase( *naomi->rbegin() );
    return res;
  }

  tuple< double, double > naomi_choose_deceitwar( set< double > *naomi, const set< double > &ken )
  {
    auto it = naomi->lower_bound( *ken.begin() );
    tuple< double, double > res;
    if( it != naomi->end() )
      {
        res = make_tuple( *it, *ken.rbegin() + 0.000001 );
        naomi->erase( it );
      }
    else
      {
        res = make_tuple( *naomi->begin(), *naomi->begin() );
        naomi->erase( naomi->begin() );
      }
    return res;
  }
}

int main()
{
  unsigned nbCases;
  cin >> nbCases;
  for( unsigned noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      unsigned n;
      cin >> n;
      set< double > naomi, ken;

      for( unsigned i = 0 ; i < n ; i++ )
        {
          double w;
          cin >> w;
          naomi.insert(w);
        }

      for( unsigned i = 0 ; i < n ; i++ )
        {
          double w;
          cin >> w;
          ken.insert(w);
        }

      set< double > naomi_bak = naomi, ken_bak = ken;

      unsigned deceitfulwar = 0, war = 0;

      for( unsigned i = 0 ; i < n ; i++ )
        {
          double chosen_naomi = naomi_choose_war( &naomi );
          double chosen_ken = ken_choose( chosen_naomi, &ken );
          if( chosen_naomi > chosen_ken )
            war++;
        }

      naomi.swap( naomi_bak );
      ken.swap( ken_bak );

      for( unsigned i = 0 ; i < n ; i++ )
        {
          double chosen_naomi, told_naomi;
          tie( chosen_naomi, told_naomi ) = naomi_choose_deceitwar( &naomi, ken );
          double chosen_ken = ken_choose( told_naomi, &ken );
          assert( ( told_naomi > chosen_ken ) == ( chosen_naomi > chosen_ken ) );
          if( chosen_naomi > chosen_ken )
            deceitfulwar++;
        }

      cout << "Case #" << noCase << ": " << deceitfulwar << " " << war << endl;
    }
  return EXIT_SUCCESS;
}
