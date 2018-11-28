@* The Shy Audience.
Our goal is to determine the minimum number of friends to invite
to ensure every audience member stands up at the end, in a
standing ovation.
Each audience member has a shyness value, which indicates how
many people must be standing before they, too, will stand.
The input is given in the form of a (potentially long) string.
We can invite as many friends as we want, but we need to report
the minimum number of friends.

Here is some boilerplate code to get us started, to read in
problems.

@(shy.cpp@>=
#include <iostream>
#include <string>
using namespace std ;
int main(int argc, char *argv[]) {
    int kases = 0 ;
    cin >> kases ;
    for (int kase=1; kase<=kases; kase++) {
    	@<Handle one case@> ;
    }
}

@ Handling a case means reading in the input and scanning it,
then processing it.

The solution is simple; we track from minimum to maximum shyness
the count of standing audience members, and whenever we need
an additional standing audience member, we nominate one of our
friends.

We store our final result in a variable named |r|.

@<Handle one case@>=
int r = 0;
int maxsiz = 0 ;
cin >> maxsiz ;
string audience ;
cin >> audience ;
int standing = 0 ;
for (int i=0; i<audience.size(); i++) {
   if (standing < i) {
      r += i - standing ;
      standing = i ;
   }
   standing += audience[i] - '0' ;
}
cout << "Case #" << kase << ": " << r << endl ;
