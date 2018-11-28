# /*
this_md5="$(md5sum < "$0" | cut -d' ' -f1)"
last_md5="$(readelf -p SOURCE_FILE_HASH "${0%.cpp}" 2>/dev/null | awk '/\[ *0\]/ { print $3 }')"
if [ "$this_md5" != "$last_md5" ]; then
g++ -pipe -Wall -Wextra -std=c++11 -g -march=native -O0 -DTHIS_MD5="\"$this_md5\"" -o "${0%.cpp}" "$0" ||
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
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{
  unsigned nbCases;
  cin >> nbCases;
  for( unsigned noCase = 1 ; noCase <= nbCases ; noCase++ )
    {
      unsigned nbWords;
      vector< string > words;

      cin >> nbWords;
      while( nbWords-- )
        {
          string word;
          cin >> word;
          words.push_back( word );
        }

      vector< vector< pair< char, unsigned > > > counts;
      for( string word: words )
        {
          counts.emplace_back();
          vector< pair< char, unsigned > > &counts_this_word = counts[ counts.size() - 1 ];

          counts_this_word.push_back( make_pair( word[0], 0 ) );

          for( char letter: word )
            {
              if( letter == counts_this_word[counts_this_word.size()-1].first )
                counts_this_word[counts_this_word.size()-1].second++;
              else
                counts_this_word.push_back( make_pair( letter, 1u ) );
            }
        }

      bool feglaWon = false;
      unsigned nbGroup = counts[0].size();
      for( auto count: counts )
        if( count.size() != nbGroup )
          feglaWon = true;

      if( !feglaWon )
        for( unsigned noGroup = 0 ; noGroup < nbGroup ; noGroup++ )
          {
            char letter = counts[0][noGroup].first;
            for( auto count: counts )
              if( count[noGroup].first != letter )
                feglaWon = true;
          }

      if( feglaWon )
        cout << "Case #" << noCase << ": Fegla Won" << endl;
      else
        {
          unsigned nbChange = 0;
          for( unsigned noGroup = 0 ; noGroup < nbGroup ; noGroup++ )
            {
              unsigned sum = 0;
              for( auto count: counts )
                  sum += count[noGroup].second;
              unsigned avg = (sum + words.size() / 2 ) / words.size();
              // map< unsigned, unsigned > occur;
              // for( auto count: counts )
              //   {
              //     map< unsigned, unsigned >::iterator it;
              //     if( ( it = occur.find( count[noGroup].second ) ) == occur.end() )
              //       occur.insert( make_pair( count[noGroup].second, 1 ) );
              //     else
              //       it->second++;
              //   }
              // unsigned sum = 0;
              // for( auto o: occur )
              //   {
              //     sum += o.second;
              //   }
              // unsigned target = sum / words.size();
              for( auto count: counts )
                {
                  nbChange += abs( (int)(count[noGroup].second - avg) );
                }
              // //              nbChange -= max;
            }

          cout << "Case #" << noCase << ": " << nbChange << endl;
        }
    }
  return EXIT_SUCCESS;
}
