@* Forest.
Calculate how many points need to be removed for a point to be
on the convex hull.  Do it for all the points.

@(for.cpp@>=
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std ;
vector<double> xa, ya ;
@<Utility routines@> ;
int main(int argc, char *argv[]) {
    int kases = 0 ;
    cin >> kases ;
    for (int kase=1; kase<=kases; kase++) {
    	@<Handle one case@> ;
    }
}

@ Handling a case means reading in the input and scanning it,
then processing it.  We'll read it first, and defer discussion
of eating until later.

@<Handle one case@>=
int N ;
cin >> N ;
xa.clear() ;
ya.clear() ;
for (int i=0; i<N; i++) {
    double x, y ;
    cin >> x >> y ;
    xa.push_back(x) ;
    ya.push_back(y) ;
}
@<Calculate result@> ;
cout << "Case #" << kase << ":" << endl ;
for (int i=0; i<N; i++)
   cout << r[i] << endl ;

@ This is probably not the fastest way but it should be fast
enough.  For each starting point, we sort the other points
using atan2().

@<Calculate result@>=
vector<int> r ;
for (int o=0; o<N; o++) {
   @<Set up sortable@> ;
   @<Sort it@> ;
   @<Scan it@> ;
}

@ To set up the sortable, we build a pair with the angle
and the 

@<Set up sortable@>=
vector<pair<double, int> > s ;
for (int i=0; i<N; i++)
   if (i != o)
      s.push_back(make_pair(atan2(xa[i]-xa[o], ya[i]-ya[o]), i)) ;

@ Sorting it is pretty easy.

@<Sort it@>=
sort(s.begin(), s.end()) ;

@ Now we can it, finding the fewest points that are
strictly within opposite angles.  A simple scan works
pretty well, but we need to be careful of the math.
At each step we advance |b| to point to the first point
that is on the other side of the line that runs from
|a| to |o|.


@<Scan it@>=
int best = s.size() ;
int a = 0 ;
int b = 0 ;
for (int a=0; a<s.size(); a++) {
   while (side(s[a].second, o, s[b].second) >= 0) {
      b++ ;
      if (b >= s.size())
         b = 0 ;
      if (b == a)
         break ;
   }
   int t = a - b ;
   if (t < 0)
      t += s.size() ;
   if (t < best)
      best = t ;
}
r.push_back(best) ;

@ We need a reliable routine to determine which side of
a point a particular point is on.

@<Utility...@>=
double side(int a, int o, int b) {
   double dax = xa[o] - xa[a] ;
   double day = ya[o] - ya[a] ;
   double dbx = xa[b] - xa[a] ;
   double dby = ya[b] - ya[a] ;
   return dax * dby - dbx * day ;
}