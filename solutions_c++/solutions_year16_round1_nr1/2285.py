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

std::vector<char> solve(const std::string& s )
{
  std::vector<char> res;
  int pos = 0;
  char lastlargest = 'A';
  while ( pos < s.length() )
  {
    char largest = s[pos];
    int lpos = pos;
    for ( int i = pos; i < s.length(); ++i )
      if ( s[i] > largest )
      {
        lpos = i;
        largest = s[i];
      }
//    printf("%c",largest);

    if ( res.size()>0&&largest<res[0])
    {
      res.insert(res.end(),&s[pos],&s[s.length()]);
      return res;
    }

    if (res.size()>0&&largest==res[0])
      res.insert(res.begin(),largest); //< left
    else
      res.insert(res.end(),largest); //< left
    if ( pos == 0 && lpos >0 )
    {
      std::vector<char> tmps = solve( s.substr(0,lpos) );
      res.insert(res.end(),tmps.begin(),tmps.end());
    }
    else
      res.insert(res.end(),&s[pos],&s[lpos]); //< right

//
//    for ( int k=pos;k<lpos;++k)
//      printf("%c",s[k]);
    pos = lpos+1;
    lastlargest = largest;
  }
  return res;
//  for ( char x : res )
//    printf("%c", x );
}

int main(int arng, char**argv)
{
  int ncase;
  scanf("%d",&ncase);
  for (int icase=0;icase<ncase;++icase)
  {
    char tmp[1002];
    scanf("%s",tmp);
    std::string s = tmp;
    printf("Case #%d: ",icase+1);
    for ( char x : solve(s) )
      printf("%c",x);
    printf("\n");
  }
  return 0;
}
