@* Ominoes.  This one looks tough.  Our usual boilerplate:

@(om.cpp@>=
#include <iostream>
#include <vector>
using namespace std ;
@<Utility routines@> ;
int main(int argc, char *argv[]) {
    int kases = 0 ;
    cin >> kases ;
    for (int kase=1; kase<=kases; kase++) {
    	@<Handle one case@> ;
    }
}

@ We read in the values, and then list all the conditions we can
think of.

@<Handle one case@>=
int X, R, C ;
cin >> X >> R >> C ;
const char *res = 0 ;
const char *RICHARD = "RICHARD" ;
const char *GABRIEL = "GABRIEL" ;

@ First, can Richard win by picking a piece that just won't fit?
The candidate would be the straight piece.

@<Handle one case@>=
if (X > R && X > C)
   res = "X too large" ;

@ We can make a polyomino with a bounding box of $i\times i$
with $X=2*i-1$; the minimum dimension must be able to cope
with this.

@<Handle one case@>=
if ((X+1)/2 > R || (X+1)/2 > C)
   res = "squarish X won't fit" ;

@ Maybe things just don't divide quite right.

@<Handle one case@>=
if (R * C % X != 0)
   res = "doesn't divide" ;

@ Can Richard pick a piece with a hole?

@<Handle one case@>=
if (X >= 7)
   res = "holy poly" ;

@ If Richard can choose a polyomino that always goes
edge to edge, then he might be able to block things
with a bad modulo value.

@<Handle one case@>=
int mindimen = (R < C ? R : C) ;
int maxdimen = (R > C ? R : C) ;
int blocker = ((X + 1) / 2) ;
if (blocker >= mindimen) {
   @<Check for a blocker@> ;
}

@ A blocker works if we can find a polyomino that
guarentees each side will not be divisible.  We can
always do this if X and the minimum dimension have a
gcd that is not one.

@<Check for a blocker@>=
if (gcd(mindimen, X) > 1)
   res = "force bad modulo with blocker" ;

@ We need our gcd routine for this.

@<Utility...@>=
int gcd(int a, int b) {
   if (a == 0)
      return b ;
   if (a > b)
      return gcd(b, a) ;
   return gcd(b % a, a) ;
}

@ We can also do it if overall we can't fit $X+1$
polyominoes in the area.  This is because we can
force any given modulus (I think) and thus force
the worst one that doesn't permit any legal split.
This only applies for sizes of 4 or larger; for 3
we can't make a piece that doesn't fit nicely on
the edge.

@<Check for a blocker@>=
if (R * C < X * (X + 1) && X > 3)
   res = "block and bad modulo" ;

@ If Richard doesn't win, Gabriel must.

@<Handle one case@>=
if (res == 0)
   res = GABRIEL ;
else
   res = RICHARD ;
cout << "Case #" << kase << ": " << res << endl ;
