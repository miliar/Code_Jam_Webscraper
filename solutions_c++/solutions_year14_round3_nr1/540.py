#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>

using namespace std;

const char infile[] = "input.in";
const char outfile[] = "output.out";

ifstream fin(infile);
ofstream fout(outfile);

const int MAXN = 100005;
const int oo = 0x3f3f3f3f;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

long long Pow[MAXN];

inline long long GCD(long long, long long);
inline void generateSolution();


int T;
long long P,Q,W;

int main() {
    cin.sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);
    #endif
	scanf("%d",&T);
    generateSolution();
	char c;
	for(int test = 1 ; test <= T; ++ test)
	{
		scanf("%lld %c %lld",&P,&c,&Q);
		W = GCD(Q,P);
		int i, j;
		P /= W;
		Q /= W;
        if(binary_search(Pow ,Pow + 42 ,Q)) {
			j = 1;
			bool o = true;
			if(P > Q) {
				printf("Case #%d: impossible\n", test);
				o = false;
			}
			while(j <= 40 && o) {
				if(P >= Q >> 1) {
					printf("Case #%d: %d\n",test,j);
					o = false;
				}
				Q >>= 1;
				++ j;
			}
			if(o == true)  printf("Case #%d: impossible\n",test);
		}
		else printf("Case #%d: impossible\n",test);

	}
    fin.close();
    fout.close();
    return 0;
}

inline long long GCD(long long a,long long b) {
	if(b == 0)
        return a;
	else return GCD(b , a%b);
}

inline void generateSolution() {
	long long i = 1 , j; Pow[0] = i;
	for(j = 1 ; j <= 11 * 4; ++ j) {
		i <<= 1;
		Pow[ j ] = i;
	}
}
