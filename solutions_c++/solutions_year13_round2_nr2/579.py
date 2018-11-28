#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <vector>

using namespace std;

int N;      // number of diamonds
int Ix, Iy; // point of interest

struct Diamond
{
  int x, y;
  Diamond(const int nx=-1, const int ny=-1):
    x(nx), y(ny) {}
  bool isNull() const { return x==-1 && y==-1; }
  Diamond& operator= (const Diamond &d)
  {
    x = d.x;
    y = d.y;
    return *this;
  }
};

bool operator== (const Diamond &a, const Diamond &b)
{
  return a.x==b.x && a.y==b.y;
}

bool operator< (const Diamond &a, const Diamond &b)
{
  if ( a.x != b.x ) return a.x < b.x;
  else              return a.y < b.y;
}

vector<Diamond> diamonds;

bool diamondExists(const Diamond &d)
{
  for ( int i=0; i<diamonds.size(); ++i )
    if ( diamonds[i] == d )
      return true;
  return false;
}

int getInitY()
{
  if ( diamonds.empty() )
    return 0;
  else {
    int max_y = 0;
    for ( vector<Diamond>::iterator it=diamonds.begin(); 
	  it!=diamonds.end(); ++it ) {
      if ( it->x == 0 )
	max_y = max(max_y, it->y);
    }
    return max_y + 2;
  }
}

double search(const int diamond_count, Diamond current_diamond)
{
  if ( diamond_count == N ) {
    if ( diamondExists( Diamond(Ix, Iy) ) )
      return 1.0;
    else
      return 0.0;
  }
  else {
    if ( current_diamond.isNull() ) {
      current_diamond.x = 0;
      current_diamond.y = getInitY();
    }
    Diamond L(current_diamond.x-1, current_diamond.y-1);
    Diamond R(current_diamond.x+1, current_diamond.y-1);
    bool L_occupied = diamondExists(L);
    bool R_occupied = diamondExists(R);
    if ( current_diamond.y==0 || (L_occupied && R_occupied) ) {
      /*
      printf("  diamond[%d] stopped at (%d, %d)\n", 
	     diamond_count, current_diamond.x, current_diamond.y);
      */
      assert( !diamondExists(current_diamond) );
      assert( current_diamond.y>=0 );

      diamonds.push_back(current_diamond);
      double probability = search(diamond_count+1, Diamond());
      diamonds.pop_back();

      return probability;
    }
    else {
      if      ( !L_occupied &&  R_occupied ) return search(diamond_count, L);
      else if (  L_occupied && !R_occupied ) return search(diamond_count, R);
      else {
	double L_probability = search(diamond_count, L);
	double R_probability = search(diamond_count, R);
	return 0.5 * L_probability
             + 0.5 * R_probability;
      }
    }
  }
}

double solve()
{
  assert(diamonds.empty());
  return search(0, Diamond());
}

void printAnswer(const double ans)
{
  char buf[16], *ptr;
  sprintf(buf, "%.8f", ans);
  ptr = buf;
  while ( *ptr!='\0' ) ++ptr;
  while ( ptr[-2]!='.' && ptr[-1]=='0' ) *--ptr='\0';
  puts(buf);
}

int main()
{
  int T;
  scanf("%d\n", &T);
  for ( int i=1; i<=T; ++i ) {
    scanf("%d %d %d\n", &N, &Ix, &Iy);
    printf("Case #%d: ", i);
    printAnswer(solve());
  }
}
