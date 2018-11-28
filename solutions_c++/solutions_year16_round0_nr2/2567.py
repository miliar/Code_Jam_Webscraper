/*
 * second.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: Nizam
 */

#include <bits/stdc++.h> // Contains all useful header files

using namespace std;

// Data types
#define ll 				long long
#define llu 			long long unsigned
#define ui				unsigned int
// Input macros
#define s(n) 			int (n); scanf("%d", &n)
#define sc(n) 			char (n); scanf("%c", &n)
#define sl(n) 			llu (n); scanf("%I64d", &n)
#define sf(n) 			double (n); scanf("%lf", &n)
#define ss(n) 			char tmp[102]; scanf("%101s", tmp); string n=tmp
// Output macros
#define p(n)			printf("%d", n)
#define pn(n)			printf("%d\n", n)
#define pl(n)			printf("%I64d ", n)
#define pln(n)			printf("%I64d\n", n)
#define pf(n)			printf("%f ", n)
#define pfn(n)			printf("%f\n", n)
#define ps(n)			cout<<n;
#define psn(n)			printf("%s\n", n)
// Useful constants
#define INF				(int)1e9
#define EPS				1e-9
// Useful hardware instructions
#define bitcount		__builtin_popcount
#define gcd				__gcd
// Useful bit manipulations
#define bit(x, i) 		(x & (1<<i))							// Select the bit of position i of x
#define lowbit(x)		((x) & ((x) ^ ((x) - 1)))				// Get the lowest bit of x
#define hBit(msb, n)	asm("bsrl %1, %0" : "=r"(msb) : "r"(n)) // Get the highest bit of x
// Inequalities
#define IN(i, l, r)		((l<i) && (i<r))
#define LIN(i, l, r)	((l<=i) && (i<r))
#define INR(i, l, r)	((l<i) && (i<=r))
#define LINR(i, l, r)	((l<=i) && (i<=r))
// Useful traversal macros
#define FR(i, l, r)		for(int i=l; i<r; i++)
#define FL(i, r, l)		for(int i=r; i>l; i--)
#define FRL(i, l, r)	for(llu i=l; i<r; i++)
#define FOREACH(i, t)	for(typeof(t.begin()) i=t.begin(); i!=t.end(); i++)	// Traverse an STL data structure
#define ALL(c)			(c).begin(), (c).end()					// For functions like sort()
#define PRESENT(c, x)	(find(ALL(c), x) != (c).end())
// For map, pair
#define mp				make_pair
#define fi				first
#define se	 			second
// For vectors
#define pb				push_back
typedef vector<int>		vi;
typedef vector<vi>		vii;
typedef pair<int, int>	ii;
// Some common useful functions
#define maX(a, b) 		((a) > (b) ? (a) : (b))
#define miN(a, b) 		((a) < (b) ? (a) : (b))
#define RESET(a, x)		memset(a, x, sizeof(a))
#define char2Int(c)		(c-'0')

int main(){
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	s(T);
	int r = T;
	while(T--){
		ss(S);

		int iter = 0;
		string sTemp = S;

		while(true){
			int found = (sTemp.find_first_of("-"));
			if(found == -1) break;
			else if(found > 0) {
				string sSub1 = sTemp.substr(0, found);
				string sSub2 = sTemp.substr(found);
				//reverse(sSub1.begin(), sSub1.end());
				string sSub3 (sSub1.size(), '-');
				sTemp = sSub3 + sSub2;
			}
			else if(found == 0) {
				int found2 = (sTemp.find_first_of("+"));
				if(found2 == -1) found2 = sTemp.size();
				string sSub1 = sTemp.substr(0, found2);
				string sSub2 = sTemp.substr(found2);
				string sSub3 (sSub1.size(), '+');
				sTemp = sSub3 + sSub2;
			}
			//pn(found);
			//ps(sTemp);ps("\n");
			iter++;
		}

		ps("Case #");p(r-T);ps(": ");pn(iter);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}


