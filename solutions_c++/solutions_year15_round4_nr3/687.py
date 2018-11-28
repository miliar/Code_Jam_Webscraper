#include <iostream>
#include <cstdio>

#include <string>
//#include <set>
#include <vector>

#include <ext/hash_set>
using __gnu_cxx::hash_set;

using namespace std;

#define FOREACH(it,c) for(__typeof__((c).begin()) it=(c).begin();it!=(c).end();++it)

int N;
vector< vector<string> > sentences;

vector<string> split(const string& s, const string& delim=" ",
                     bool discard_empty=true) {
   vector<string> ret;
   size_t p0 = 0;
   while (true) {
      if (discard_empty) {
         p0 = s.find_first_not_of(delim, p0);
         if (p0 == string::npos)
           break;
      }

      size_t p = s.find_first_of(delim, p0);
      if (p == string::npos)
         break;
      ret.push_back(s.substr(p0, p-p0));
      p0 = p+1;
   }
   if (p0 != string::npos)
      ret.push_back(s.substr(p0));
   return ret;
}

struct djb_hash_string {
   size_t operator() ( const string& key ) const {
      size_t h = 0;
      for ( int i = 0; i < (int) key.size(); ++i )
      // h = 33 * h + key[i];
         h = 33 * h ^ key[i];
      return h;
   }
};

typedef hash_set< string, djb_hash_string > HS;

int main(int argc, char* argv[]) {
   string line;

   int TC;
   getline(cin, line);
   sscanf(line.c_str(), "%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      getline(cin, line);
      sscanf(line.c_str(), "%d", &N);
      sentences = vector< vector<string> >(N);
      for (int i = 0; i < N; ++i) {
         getline(cin, line);
         sentences[i] = split(line);
      }

      HS eng;
      for (int j = 0; j < (int) sentences[0].size(); ++j) {
         eng.insert( sentences[0][j] );
      }
      HS fr;
      for (int j = 0; j < (int) sentences[1].size(); ++j) {
         fr.insert( sentences[1][j] );
      }
      
/*
      FOREACH(it, eng) {
         cerr << *it << ' ';
      }
      cerr << endl;

      FOREACH(it, fr) {
         cerr << *it << ' ';
      }
      cerr << endl;
*/

      HS C;
      FOREACH(it, fr) {
         if (eng.count(*it))
            C.insert(*it);
      }

      sentences.erase( sentences.begin(), sentences.begin()+2 );

      int res = 1000000000;
      N -= 2;
      for (int mask = (1<<N)-1; mask >= 0; --mask) {
         HS eng2, fr2;
         for (int i = 0; i < N; ++i) {
            if (mask & (1<<i)) {
               // English
               for (int j = 0; j < (int) sentences[i].size(); ++j) {
                  if (eng.count(sentences[i][j]) == 0)
                     eng2.insert( sentences[i][j] );
               }
            }
            else {
               // French
               for (int j = 0; j < (int) sentences[i].size(); ++j) {
                  if (fr.count(sentences[i][j]) == 0)
                     fr2.insert( sentences[i][j] );
               }
            }
         }

         HS C2;
         FOREACH(it, fr2) {
            if (C.count(*it) == 0 && (eng2.count(*it) || eng.count(*it))) {
               C2.insert(*it);
            }
         }
         FOREACH(it, eng2) {
            if (C.count(*it) == 0 && (fr2.count(*it) || fr.count(*it))) {
               C2.insert(*it);
            }
         }
         res = min(res, (int) (C.size() + C2.size()));
      }

      cout << "Case #" << tc << ": " << res << "\n";
   }

   return 0;
}
