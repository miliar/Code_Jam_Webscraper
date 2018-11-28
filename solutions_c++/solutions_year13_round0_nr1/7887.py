#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

const char charmap[] = ".XOT";

struct board
{
  unsigned long data;
  bool hasEmpty;
  
  board() : data(0), hasEmpty(false) {};
  
  inline char get(int x, int y)
  {
    return charmap[(data >> ((y*4+x)*2) ) & 3];
  }
  
  void debug()
  {
    cout << "------------------------ " << hex << data << endl;
    for ( int y = 0; y < 4; ++y )
    {
      for ( int x = 0; x < 4; ++x )
        cout << get(x,y);
      cout << endl;
    }
    cout << "------------------------" << endl;
  }
  
  inline void set(int x, int y, char c)
  {
    //data &= ~(3 << ((y*4+x)*2));  // clear
    size_t id = ((find(charmap,charmap+sizeof(charmap), c) - charmap)&3);
    data |= id << ((y*4+x)*2);  // set
    if ( id == 0 )
      hasEmpty = true;
  }
  bool isXWinner()
  {
    return  (data & 0x55           ) == 0x55            ||
            (data & 0x5500         ) == 0x5500          ||
            (data & 0x550000       ) == 0x550000        ||
            (data & 0x55000000     ) == 0x55000000      ||
            (data & 0x40404040     ) == 0x40404040      ||
            (data & (0x40404040>>2)) == (0x40404040>>2) ||
            (data & (0x40404040>>4)) == (0x40404040>>4) ||
            (data & (0x40404040>>6)) == (0x40404040>>6) ||
            (data & 0x40100401     ) == 0x40100401      ||
            (data & 0x01041040     ) == 0x01041040;
  }
  bool isOWinner()
  {
    return  (data & (0x55<<1)      ) == (0x55<<1)       ||
            (data & (0x5500<<1)    ) == (0x5500<<1)     ||
            (data & (0x550000<<1)  ) == (0x550000<<1)   ||
            (data & (0x55000000<<1)) == (0x55000000<<1) ||
            (data & 0x80808080     ) == 0x80808080      ||
            (data & (0x80808080>>2)) == (0x80808080>>2) ||
            (data & (0x80808080>>4)) == (0x80808080>>4) ||
            (data & (0x80808080>>6)) == (0x80808080>>6) ||
            (data & 0x80200802     ) == 0x80200802      ||
            (data & (0x01041040<<1)) == (0x01041040<<1);
  }
};

int main()
{
  
  int T;
  cin >> T;
  unsigned c = 0;
  while ( T-- )
  {
    string s;
    board b;
    for ( int i = 0; i < 4; ++i )
    {
      cin >> s;
      for ( int j = 0; j < min(s.length(), 4U); ++j )
        b.set(j, i, s[j]);
    }
    
    //b.debug();
    
    cout << "Case #" << (++c) << ": ";
    if ( b.isXWinner() )
      cout << "X won" << endl;
    else if ( b.isOWinner() )
      cout << "O won" << endl;
    else if ( b.hasEmpty )
      cout << "Game has not completed" << endl;
    else
      cout << "Draw" << endl;
  }

}
