#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <limits>
#include <complex>
#include <deque>

using namespace std;

// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9

// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;++i)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))

#define ull							unsigned long long
#define ll							long long
#define mp                          make_pair
#define pb                          push_back

// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

#ifdef DEBUG
     #define debug(args...)            {dbg,args; cerr<<endl;}
#else
    #define debug(args...)              // Just strip off all debug tokens
#endif
struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

/*----------------------------------------------------------------------------------------------------------*/

int caseNumber = 1;

void printSolution();

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	++T;

	while(caseNumber != T) {
		printSolution();
		++caseNumber;
	}
	return 0;
}

void printSolution(){
	cout << "Case #" << caseNumber << ": ";
	string str;
	cin >> str;

	deque<char> result;
	
	result.push_front(str[0]);
	for (int i = 1; i != str.size(); ++i) {
		if (str[i] >= result[0]) {
			result.push_front(str[i]);
		} else {
			result.push_back(str[i]);
		}
	}

	string tt(all(result));
	cout << tt << "\n";

}