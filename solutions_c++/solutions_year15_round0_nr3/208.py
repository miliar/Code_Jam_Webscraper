@* Dijkstra.
We are playing with quaternion math here.

Here is some boilerplate code to get us started, to read in
problems.

@(ijk.cpp@>=
#include <iostream>
#include <string>
@<Quaternion math@> ;
using namespace std ;
int main(int argc, char *argv[]) {
    @<Initialize@> ;
    int kases = 0 ;
    cin >> kases ;
    for (int kase=1; kase<=kases; kase++) {
    	@<Handle one case@> ;
    }
}

@ Handling a case means reading in the input and scanning it,
then processing it.

@<Handle one case@>=
int L ;
long long X ;
string s ;
cin >> L >> X >> s ;

@ The core of this problem is quaternion math.  We use an
enum and a multiplication table to help us with it.  There
are eight values.  We define these so negation is just
exclusive or'ing with 4.

@<Quaternion math@>=
enum quat { ONE, I, J, K, NEGONE, NEGI, NEGJ, NEGK, QUATSIZE } ;
quat mul[QUATSIZE][QUATSIZE] = {
   { ONE, I, J, K },
   { I, NEGONE, K, NEGJ },
   { J, NEGK, NEGONE, I },
   { K, J, NEGI, NEGONE }
} ;

@ We also need something to translate from $i$, $j$, and $k$
to the quaternion enumeration.  We will assume ASCII input
here.

@<Quaternion math@>=
quat quatValue[128] ;

@ We need a routine to expand the table from 4x4 to 8x8.
We also need to fill in the quatValue table.  A value of
|QUATSIZE| indicates we fell off the world.

@<Quaternion math@>=
void initquat() {
   for (int i=0; i<4; i++) {
      for (int j=0; j<4; j++) {
         mul[i+4][j+4] = mul[i][j] ;
	 mul[i][j+4] = mul[i+4][j] = (quat)(4 ^ mul[i][j]) ;
      }
   }
   for (int i=0; i<sizeof(quatValue)/sizeof(quatValue[0]); i++)
      quatValue[i] = QUATSIZE ;
   quatValue['i'] = I ;
   quatValue['j'] = J ;
   quatValue['k'] = K ;
}

@ We need to call that initialization routine.

@<Initialize@>=
initquat() ;

@ Now we can get back to solving.  If there is a string prefix
that attains the value $i$, then every longer string prefix
that attains the value $i$ will be different only by a suffix
that is equal to the value $1$.  Therefore, all we need to do
is find the first prefix that equals $i$, if any, then the
first subsequent substring that equals $j$, and then make
sure the rest of the string equals $k$.

Instead of that last, it's simpler just to ensure the whole
string multiplies out to $ijk$ which is $-1$ itself.  We can
do this first to save some search.  Luckily doing exponentiation
is pretty quick.  So we'll write that code next.

@<Handle one case@>=
quat sval = ONE ;
for (int i=0; i<s.size(); i++)
   sval = mul[sval][quatValue[s[i]]] ;
quat fullValue = ONE ;
quat smul = sval ;
for (long long multiplier=X; multiplier; multiplier >>= 1) {
    if (multiplier & 1)
       fullValue = mul[fullValue][smul] ;
    smul = mul[smul][smul] ;
}

@ Now we get into the hard work.  We repeatedly scan the
string, looking for a way to attain $i$, then $j$.  But
if we ever get back to the front of the string with a
value we've seen before, we're looping so we can immediately
terminate the search.

We keep track of the starting points of the strings with
a mask.

We only do any of this if the overall product was found to
be one.

@<Handle one case@>=
bool okay = false ;
if (fullValue == NEGONE) {
   quat curVal = ONE ;
   quat search = I ;
   int seenMask = 0 ;
   for (long long iX = 0; iX<X && !okay; iX++) {
      if ((seenMask >> curVal) & 1) // repeat; stop!
         break ;
      seenMask |= 1<<curVal ;
      for (int iL = 0; iL<L; iL++) {
         curVal = mul[curVal][quatValue[s[iL]]] ;
         if (curVal == search) {
            seenMask = 0 ; // reset the seen mask!
	    curVal = ONE ;
	    if (search == I) {
	       search = J ;
            } else if (search == J) { // we found I and J
               okay = true ;
	       break ;
            } else {
	       throw "Bad value for search??" ;
            }
         }
      }
   }
}

@ The only thing remaining is to report success or failure.

@<Handle one case@>=
cout << "Case #" << kase << ": " << (okay ? "YES" : "NO") << endl ;
