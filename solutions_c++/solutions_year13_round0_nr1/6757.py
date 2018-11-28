#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

class Board {
  char map[16];
public:
  Board() {
    for ( int i=0; i < 16; i++ ) map[i]='.';
  }
  friend istream & operator>>(istream & in, Board & board);
  friend ostream & operator<<(ostream & out, const Board & board);
};

istream & operator>>(istream & in, Board & board)
{
  char c;
  int count = 0;
  while ( count < 16 )
  {
    do { cin >> c; } while ( isspace(c) );
    board.map[count++] = (isalpha(c) ? toupper(c) : c);
  }
  return in;
}

inline bool isOWin(const string & s)
{
  bool ans = true;
  for ( int i=0; i < 4; i++ )
    if ( !(s[i] == 'O' || s[i] == 'T') ) ans = false;
  return ans;
}

inline bool isXWin(const string & s)
{
  bool ans = true;
  for ( int i=0; i < 4; i++ )
    if ( !(s[i] == 'X' || s[i] == 'T') ) ans = false;
  return ans;
}

inline bool hasDot(const string & s)
{
  for ( int i=0; i < 4; i++ )
    if ( s[i] == '.' ) return true;
  return false;
}

ostream & operator<<(ostream & out, const Board & board)
{
  /*
  out << endl;
  for ( int i=0; i < 4; i++ )
  {
    for ( int j=0; j < 4; j++ )
      out << board.map[i*4+j];
    out << endl;
  }
  */
  vector<string> vs;
  const char * p = board.map;
  for ( int i=0; i < 4; i++ ) {
    char b[4] = {p[i*4+0], p[i*4+1], p[i*4+2], p[i*4+3]};
    string s(b);
    vs.push_back(s);
  }
  for ( int i=0; i < 4; i++ ) {
    char b[4] = {p[i+0], p[i+4], p[i+8], p[i+12]};
    string s(b);
    vs.push_back(s);
  }
  {
    char b[4] = {p[0], p[5], p[10], p[15]};
    string s(b);
    vs.push_back(s);
  }
  {
    char b[4] = {p[3], p[6], p[9], p[12]};
    string s(b);
    vs.push_back(s);
  }
  for ( size_t i=0; i < vs.size(); i++ )
    if ( isOWin(vs[i]) ) { out << "O won";return out; }
  for ( size_t i=0; i < vs.size(); i++ )
    if ( isXWin(vs[i]) ) { out << "X won";return out; }
  for ( size_t i=0; i < vs.size(); i++ )
    if ( hasDot(vs[i]) ) { out << "Game has not completed";return out; }
  out << "Draw";
  return out;
}

int main()
{
  int T, rT=0;
  cin >> T;
  Board board;
  while ( rT++ != T )
  {
    cin >> board;
    cout << "Case #" << rT << ": " << board << std::endl;
  }
  return 0;
}
