#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cassert>
#include <bitset>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <sstream>

struct Pass {
  int64_t o;
  int64_t e;
  int64_t p;
};

struct Event {
  int64_t pos;
  int64_t p_ref;
  bool out;
  bool operator<( const Event& e ) const
  {
    return pos < e.pos || ( pos==e.pos && ((int)out<(int)e.out)  );
  }
};

int64_t pay( int64_t from, int64_t to, int64_t N )
{
  int64_t res = 0;
  for (int64_t i=from; i<to; ++i)
  {
    res += N;
    --N;
  }
  return res;
}

int main( int argn, char** argv )
  {
    int ncases;
    scanf("%d",&ncases);
    for ( int icase = 0; icase<ncases; ++icase )
    {
      int N,M;
      scanf("%d%d",&N,&M);

      std::vector< Pass > traff;
      for (int i=0; i<M; ++i)
      {
	int64_t o, e, p;
	scanf("%ld%ld%ld", &o, &e, &p );
	Pass pass;
	pass.o = o;
	pass.e = e;
	pass.p = p;
	traff.push_back( pass );
      }
      std::sort( traff.begin(), traff.end(), []( const Pass& lhs, const Pass& rhs ) { return lhs.o < rhs.o; }  );

      int64_t normal_pay = 0;

      std::vector< Event > ct;
      for ( unsigned i =0; i<traff.size(); ++i)
      {
	normal_pay += pay( traff[i].o, traff[i].e, N ) * traff[i].p;
	Event e;
	e.pos = traff[i].o;
	e.p_ref = i;
	e.out = false;
	ct.push_back( e );
	e.out = true;
	e.pos = traff[i].e;
	ct.push_back( e );
      }
      std::sort( ct.begin(), ct.end() );

      int64_t cheat_pay = 0;
      std::vector< Pass > curpass;
      for ( unsigned i = 0; i< ct.size(); ++i )
      {
	if ( ! ct[i].out )
	  curpass.push_back( traff[ ct[i].p_ref ] );
	else
	{
	  // use the passanger cards of the smallest origin
	  int64_t num_persons = traff[ ct[i].p_ref ].p;
	  std::sort( curpass.begin(), curpass.end(), []( const Pass& lhs, const Pass& rhs ) { return lhs.o > rhs.o; } );
	  auto it = curpass.begin();
	  while ( num_persons > 0 )
	  {
	    if ( it == curpass.end() )
	      printf("XXXXXXXX\n");
	    int64_t raus = std::min( num_persons, it->p );
	    it->p -= raus;
	    num_persons -= raus;
	    if ( raus > 0 )
	      cheat_pay += raus * pay( it->o, ct[i].pos, N );
	    ++it;
	  }
	}
      }
//      printf("normal: %ld cheat: %ld\n",normal_pay,cheat_pay);
      printf("Case #%d: %ld\n",icase+1,(normal_pay-cheat_pay)%1000002013);
    }
    return 0;
  }
