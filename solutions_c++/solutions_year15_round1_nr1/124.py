@* Mushrooms.
Instead of pancakes, this time we have mushrooms.  But our
boilerplate code is much the same.

@(mush.cpp@>=
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
int N ;
vector<int> p ;
cin >> N ;
for (int i=0; i<N; i++) {
    int t ;
    cin >> t ;
    p.push_back(t) ;
}
@<Calculate result1@> ;
@<Calculate result2@> ;
cout << "Case #" << kase << ": " << result1 << " " << result2 << endl ;

@ To calculate the first result, we just accumulate all the times
mushrooms disappear (the count decreases).

@<Calculate result1@>=
long long result1 = 0 ;
for (int i=0; i+1<N; i++)
    if (p[i+1] < p[i])
        result1 += p[i] - p[i+1] ;

@ For the second result, we find the maximum decrease, and assume
that for all the seconds.  We do have to scan and make sure she
never eats more in any second than she can, however.

@<Calculate result2@>=
long long result2 = 0 ;
int rate = 0 ;
for (int i=0; i+1<N; i++)
    if (p[i+1] < p[i] && p[i] - p[i+1] > rate)
       rate = p[i] - p[i+1] ;
for (int i=0; i+1<N; i++) {
    if (p[i] >= rate)
        result2 += rate ;
    else
        result2 += p[i] ;
}
