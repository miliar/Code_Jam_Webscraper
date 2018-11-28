@* Pancakes.
In this problem, everyone has pancakes.  We can spend a certain
amount of time splitting the stacks, or we can just let people
eat.  Again, some boilerplate to get things started.

@(pan.cpp@>=
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
of eating until later.  We do determine the largest stack,
since this gives us a high point for our split.

@<Handle one case@>=
int best = 1000000 ; // never more pancakes than this
int D ;
vector<int> p ;
cin >> D ;
int maxD = 0 ;
for (int i=0; i<D; i++) {
    int t ;
    cin >> t ;
    p.push_back(t) ;
    if (t > maxD)
       maxD = t ;
}
@<Calculate best split@> ;
cout << "Case #" << kase << ": " << best << endl ;

@ The first observation we make is it is always beneficial to
do all splitting up front, since then we use as many mouths
as possible to actually do the eating.

Once all splitting is done, the only thing that matters is
the final height of the final stack.  And for every possible
final height, we can easily determine how many splits we
might need to do.

So we just use brute force, iterating over all possible split
points.  This could easily be made faster, but simplicity
often wins.

@<Calculate best split@>=
for (int split=1; split<=maxD; split++) {
    int splitCount = 0 ;
    for (int i=0; i<p.size(); i++)
       splitCount += (p[i] - 1) / split ;
    if (split + splitCount < best)
       best = split + splitCount ;
}
