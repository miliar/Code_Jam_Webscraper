# /*
this_md5="$(md5sum < "$0" | cut -d' ' -f1)"
last_md5="$(readelf -p SOURCE_FILE_HASH "${0%.cpp}" 2>/dev/null | awk '/\[ *0\]/ { print $3 }')"
if [ "$this_md5" != "$last_md5" ]; then
g++ -pipe -Wall -Wextra -std=c++11 -g -march=native -O3 -DTHIS_MD5="\"$this_md5\"" -o "${0%.cpp}" "$0" ||
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

using namespace std;

int main()
{
  unsigned nbCases;
  cin >> nbCases;
  for( unsigned noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      unsigned a, b, k, n = 0;
      cin >> a >> b >> k;
      for( unsigned ai = 0 ; ai < a ; ai++ )
        for( unsigned bi = 0 ; bi < b ; bi++ )
          for( unsigned ki = 0 ; ki < k ; ki++ )
            if( ( ai & bi ) == ki )
              n++;
      cout << "Case #" << noCase << ": " << n << endl;
    }
  return EXIT_SUCCESS;
}
