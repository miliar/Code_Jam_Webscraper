@* Barbers.
This is just a disguised binary search; we bin search on when
we will be served, and from that compute which barber will
serve us.

@(barb.cpp@>=
#include <iostream>
#include <vector>
using namespace std ;
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
int B, N ;
vector<int> m ;
cin >> B >> N ;
for (int i=0; i<B; i++) {
    int t ;
    cin >> t ;
    m.push_back(t) ;
}
@<Calculate result@> ;
cout << "Case #" << kase << ": " << r << endl ;

@ We binary search on when we will be seated.  We find the
earliest time $t$ such that $N$ or more people are seated;
this is the time we are seated.

@<Calculate result@>=
long long mytime = (1LL << 61) - 1 ;
for (long long b = 1LL << 60; b; b >>= 1) {
   long long ttime = mytime & ~b ;
   long long seated = 0 ;
   for (int i=0; i<B; i++) {
       seated += 1 + ttime / m[i] ;
       if (seated >= N)
          break ;
   }
   if (seated >= N)
      mytime = ttime ;
}

@ Now that we have the time, we figure out which
barber will seat us.  We first calculate how
many were seated in the time before us, and then
we iterate again and figure out which barber is
the one for us.

@<Calculate result@>=
long long seated = 0 ;
int r = -1 ;
if (mytime > 0)
   for (int i=0; i<B; i++)
      seated += 1 + (mytime - 1) / m[i] ;
for (int i=0; i<N; i++)
   if (mytime % m[i] == 0) {
      seated++ ;
      if (seated == N) {
         r = i + 1 ;
         break ;
      }
   }
